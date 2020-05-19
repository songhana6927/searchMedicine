import requests
from bs4 import BeautifulSoup as BS
import ssl
import urllib.request
import urllib.parse
import traceback

def search_google(target,start):
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
    hdr = {'User-Agent': 'Mozilla/5.0'}

    query_string = urllib.parse.urlencode(values)
    req = urllib.request.Request(base_url + '?' + query_string, headers=hdr)
    context = ssl._create_unverified_context()

    try:
        res = urllib.request.urlopen(req, context=context)
    except:
        traceback.print_exc()

    tml_data = BS(res.read(), 'html.parser')
    result_parse_data(tml_data,target,start)


def result_parse_data(tml_data,target,start):
    link = ""
    korean_nm = ""
    eng_nm = ""
    g_dang = ""
    ingradint = ""

    atags = tml_data.findAll("a")
    # 링크가 druginfo 포함하는지 확인
    for item in atags:
        # print(start)
        # print(item)
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
                ingradint  = ""
                for i in info_arr:
                    i = i.text.replace('\n','').replace('\r','').replace('\t','').strip()
                    if len(i) > 0:
                        if "당" in i or "정" in i:
                            g_dang = i
                        else:
                            ingradint = ingradint+","+i
                ingradint = ingradint[1:]
                #결과
                print("link:" + link)
                print("한글명:" + korean_nm)
                print("영문명:" + eng_nm)
                print("g당:" + g_dang)
                print("성분:" + ingradint)
            break

    #없을시 다음페이지 10 페이지 까지만
    if len(korean_nm) < 1 and start < 99:
        start = start+10
        search_google(target,start)





tml_data = search_google("클래마신건조시럽125mg/5ml",0)