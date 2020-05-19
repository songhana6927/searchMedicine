import datetime
from random import randint
import re
import requests
from bs4 import BeautifulSoup as BS
import ssl
import urllib.request
import urllib.parse
import traceback
import time

from com.mylist_behind import myMedi_select
from operator import itemgetter

def search_google(target,start,site):
    base_url = 'https://www.google.co.kr/search'
    #: 검색조건 설정
    values = {
        'q': target, # 검색할 내용
        'oq': target,
        'aqs': 'chrome..69i57.35694j0j7',
        'sourceid': 'chrome',
        'ie': 'UTF-8',
        'start': start
    }
    # Google에서는 Header 설정 필요
    hdr =  {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_5) AppleWebKit 537.36 (KHTML, like Gecko) Chrome",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8"}

    query_string = urllib.parse.urlencode(values)
    #사용자가 접속하는 것처럼 램덤 값 사용
    MAX_SLEEP_TIME = 5
    rand_value = randint(1, MAX_SLEEP_TIME)
    time.sleep(rand_value)
    req = urllib.request.Request(base_url + '?' + query_string, headers=hdr)
    context = ssl._create_unverified_context()

    try:
        res = urllib.request.urlopen(req, context=context)
    except:
        traceback.print_exc()

    tml_data = BS(res.read(), 'html.parser')
    rtn_data = ""
    if site == "druginfo":
        rtn_data = result_parse_data(tml_data,target,start)
    elif site == "kmle":
        rtn_data = result_parse_data_kmle(tml_data,target,start)

    return rtn_data


def result_parse_data(tml_data,target,start):
    link = ""
    korean_nm = ""
    eng_nm = ""
    g_dang = ""
    ingradint = ""
    myData_list = ""

    atags = tml_data.findAll("a")
    # 링크가 druginfo 포함하는지 확인
    for item in atags:
        href = item.attrs['href']
        link = urllib.parse.unquote(href)
        search = "www.druginfo.co.kr"
        if search in link:
            # 열어서 정보 확인
            link = link.replace("/url?q=","")
            linkResult = requests.get(link)
            subPage = BS(linkResult.content,"html.parser")
            title = subPage.find("title").text
            if "약품 정보" in title:
                product_tbl = subPage.find("table",{"bgcolor" : "E7E8E9"})
                b_tag = product_tbl.find("b")
                names = b_tag.contents
                korean_nm = names[0].text
                eng_nm = names[3].replace('\n','').replace('\r','').replace('\t','').strip()
                # 제조사,판매사
                sales_tbl = product_tbl.findAll("table")[1]
                # 성분,함량
                ingradint_tbl = product_tbl.findAll("table")[4].findAll("table")[1]
                info_arr = ingradint_tbl.findAll("td")
                g_dang = ""
                ingradint_  = ""
                for i in info_arr:
                    i = i.text.replace('\n','').replace('\r','').replace('\t','').strip()
                    if len(i) > 0:
                        if "당" in i or "정" in i:
                            g_dang = i
                        else:
                            ingradint_ = ingradint_+","+i
                ingradint_ = ingradint_[1:]

                ingradint = re.sub(r'\([^)]*\)', '', ingradint_)
                # 찾았으면 내 데이터도 찾아오기
                myData_list = myMedi_select(ingradint)


                # 성분이 괄호가 있는지 검사하여 있는 경우 한번 더 돌려야함
                if ("로서" in str(ingradint_)) or (" as " in str(ingradint_)):
                    ingra_array = ingradint_.split(",")
                    poham_ingradint = ""
                    for ingra_item in ingra_array:
                        if "로서" in str(ingra_item):
                            as_text = ingra_item.split('(', 1)[1].split(')')[0].replace("로서", "").replace(" as ", "")
                            poham_ingradint = poham_ingradint + "," + str(as_text)
                        elif " as " in str(ingra_item):
                            as_text = ingra_item.split(' ')
                            poham_ingradint = poham_ingradint + "," + str(as_text[2])+str(as_text[0])
                        else:
                            poham_ingradint = poham_ingradint + "," + str(ingra_item)

                    myData_list = myData_list + myMedi_select(poham_ingradint)
                    myData_list = sorted(myData_list, key=itemgetter(13), reverse=True)

                #print(myData)
                #print("link:" + link)
                #print("한글명:" + korean_nm)
                #print("영문명:" + eng_nm)
                #print("g당:" + g_dang)
                #print("성분:" + ingradint)
                #print("myData_str:" + myData_str)
            break
        else:
            link = ""



    return {"target":target,"link":link,"korean_nm":korean_nm,"eng_nm":eng_nm,"g_dang":g_dang,"ingradint":ingradint,"myData_list":myData_list}



def result_parse_data_kmle(tml_data,target,start):
    link = ""
    korean_nm = ""
    eng_nm = ""
    g_dang = ""
    ingradint = ""
    myData_list = ""

    atags = tml_data.findAll("a")
    # 링크가 druginfo 포함하는지 확인
    for item in atags:
        href = item.attrs['href']
        link = urllib.parse.unquote(href)
        search2 = "www.kmle.co.kr"
        if search2 in link:
            # 열어서 정보 확인
            link = link.replace("/url?q=","")
            linkResult = requests.get(link)
            subPage = BS(linkResult.content,"html.parser")
            title = subPage.find("title").text
            if "KMLE 약품/의약품 검색" in title:
                product_div = subPage.find("div",{"class" : "panel-body"})
                p_info = product_div.find("p")
                p_contents = p_info.contents
                korean_nm = re.sub(r'\([^)]*\)', '', p_contents[2])[2:]
                if '(' in p_contents[2]:
                    eng_nm = p_contents[2].split('(', 1)[1].split(')')[0]
                else:
                    eng_nm = ""
                ingradint = p_contents[36].strip()
                myData_list = myMedi_select(ingradint)

                #print(p_contents)
                #print("link:" + link)
                #print("한글명:" + korean_nm)
                #print("영문명:" + eng_nm)
                #print("g당:" + g_dang)
                #print("성분:" + ingradint)
                #print("myData_str:" + myData_str)
            break

        else:
            link = ""

    return {"target": target, "link": link, "korean_nm": korean_nm, "eng_nm": eng_nm, "g_dang": g_dang,"ingradint": ingradint, "myData_list": myData_list}


#print(mylist_select_to_html("phenterminehydrochloride37.5mg"))
#tml_data = search_google("클래마신건조시럽125mg/5ml",0)
#print(search_google("클래마신건조시럽125mg/5ml",0))
#("디프렌캡슐20mg",0)
#print("마노엘정"[:2])


#print(search_google("클래신건조시럽125mg/5ml",0,"druginfo"))
#print(search_google("마노엘정",0,"kmle"))
#sorted(mylist,key=lambda student: student[13])
#print(search_google("카푸린에스정",0))
