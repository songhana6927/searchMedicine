import requests
from bs4 import BeautifulSoup

def get_bs_obj(company_code):
    url = "https://finance.naver.com/item/main.nhn?code="+company_code
    result = requests.get(url)
    bs_obj = BeautifulSoup(result.content, "html.parser")
    return bs_obj

#bs_obj 를 받아서 price를 return
def get_price(company_code):
    bs_obj = get_bs_obj(company_code)
    no_today = bs_obj.find("p", {"class": "no_today"})
    blind_now = no_today.find("span", {"class": "blind"})
    return blind_now.text


# samsung 005930
# hynix   000660
# samyoung 005680
# price = get_price("005680")
cimpany_codes = {"005930","000660","005680"}
for item in cimpany_codes:
    price = get_price(item)
    print(price)