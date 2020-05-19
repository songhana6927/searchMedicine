# https://www.ncbi.nlm.nih.gov/pubmed/?term=(%22acute+Myeloid+Leukemia%22)+OR+%22AML%22
import requests
from bs4 import BeautifulSoup

url="https://www.ncbi.nlm.nih.gov/pubmed/?term=(%22acute+Myeloid+Leukemia%22)+OR+%22AML%22"
result = requests.get(url)
bs_obj = BeautifulSoup(result.content,"html.parser")
content = bs_obj.find("div",{"class": "content"})
rprts = content.findAll("div",{"class":"rprt"})

for item in rprts:
    atag = item.find("a")["href"]
    link = "https://www.ncbi.nlm.nih.gov"+atag
    linkResult = requests.get(link)
    subPage = BeautifulSoup(linkResult.content,"html.parser")
    title = subPage.find("div",{"class":"rprt_all"}).find("h1")
    print(title.text)