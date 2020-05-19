import requests
from bs4 import BeautifulSoup

#네이버 금융에서 시,고,저,종 챠트 가격 가져오기

def get_bs_obj(company_code):
    url = "https://finance.naver.com/item/main.nhn?code="+company_code
    result = requests.get(url)
    bs_obj = BeautifulSoup(result.content, "html.parser")
    return bs_obj

#bs_obj 를 받아서 price를 return
def get_candle_chart_data(company_code):
    bs_obj = get_bs_obj(company_code)
    td_first = bs_obj.find("td",{"class","first"})
    blind = td_first.find("span",{"class","blind"})

    #close 종가
    close = blind.text

    #hight 고가
    table = bs_obj.find("table",{"class","no_info"})
    trs = table.findAll("tr")
    first_tr = trs[0]
    first_tr_tds = first_tr.findAll("td")
    first_tr_tds_second_td = first_tr_tds[1]
    hight = first_tr_tds_second_td.find("span",{"class":"blind"}).text
    
    #open 시가
    open = trs[1].find("td",{"class":"first"}).find("span",{"class":"blind"}).text

    #low 저가
    low = trs[1].findAll("td")[1].find("span",{"class":"blind"}).text

    return {"close":close,"hight":hight,"open":open,"low":low}

company_codes = ["000660","035420","034220"]
for item in company_codes :
    candle_chart_data = get_candle_chart_data(item)
    print(candle_chart_data)