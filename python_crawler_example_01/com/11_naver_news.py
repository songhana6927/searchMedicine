
import urllib.request
import bs4
url = "https://news.naver.com/"
html = urllib.request.urlopen(url)

bsObj = bs4.BeautifulSoup(html,"html.parser")

ul = bsObj.find("ul",{"class":"hdline_article_list"})
lis = ul.findAll("li")
#array 만들떄
titles = [li.find("div",{"class","hdline_article_tit"}).find("a").text.strip() for li in lis]
print(titles)

for li in lis:
    title = li.find("div",{"class","hdline_article_tit"}).find("a").text.strip()
    print(title)