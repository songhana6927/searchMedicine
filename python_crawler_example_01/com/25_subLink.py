# # 서브페이지에서 데이터 수집하기
# # * 서브페이지의 데이터를 수집하려면 서브페이지의 링크를알아야 합니다
# # * 서브 url 수집하기
# # * http://www.netd.ac.za/ 크롤링
# #
# # # 페이지 분석
# # * ol -> findAll("li")-> for li.find("a")

import requests
from bs4 import BeautifulSoup

#url = "http://www.netd.ac.za/?action=browse&category=Affiliation&order=asc"
url = "http://www.netd.ac.za/portal/?action=browse&category=Affiliation&maxresults=10&start=11&order=asc"
result = requests.get(url)
bs_obj = BeautifulSoup(result.content,"html.parser")
# http://www.netd.ac.za/?action=view&identifier=oai%23Aunion.ndltd.org%3Atut%2Foai%3Aencore.tut.ac.za%3Ad1001784

ol = bs_obj.find("ol")
lis = ol.findAll("li")
for li in lis:
    ############################### 속성꺼내기 ["href"]
    print("http://www.netd.ac.za/" + li.find("a")["href"])
