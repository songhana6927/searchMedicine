# bs4 alt+enter로 설치
'''
import bs4
html_str = "<html><div></div></html>"
bsObj = bs4.BeautifulSoup(html_str,"html.parser")

print(type(bsObj))
print(bsObj)
print(bsObj.find("div"))
'''

import urllib.request
import bs4
url = "https://www.naver.com/"
html = urllib.request.urlopen(url)

bsObj = bs4.BeautifulSoup(html,"html.parser")
# print(html.read())
# print(bsObj)
#
# top_right = bsObj.find("div",{"class" : "area_links"})
# first_a = bsObj.find("a",{"class" : "al_favorite"})

ul = bsObj.find("ul",{"class":"an_l"})
lis = ul.findAll("li") # [<li></li>,<li></li>] array로 찾아줌

for li in lis:
    an_txt = li.find("span",{"class":"an_txt"})
    print(an_txt.text)


