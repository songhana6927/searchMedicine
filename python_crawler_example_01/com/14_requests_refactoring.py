# 리팩토링 : 구조를 이쁘게 바꾸면서 기능을 유지
#           왜하는가?
# crawling 하는 코드
import requests
from bs4 import BeautifulSoup

# url을 넣어서 bs_obj를 return 하는 펑션
def get_bs_obj(url):
    result  = requests.get(url)
    bs_obj = BeautifulSoup(result.content, "html.parser")
    return bs_obj

url = "https://finance.naver.com/item/main.nhn?code=005930"
bs_obj = get_bs_obj(url)
print(bs_obj)


