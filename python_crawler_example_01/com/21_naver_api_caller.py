import requests
from urllib.parse import quote
import urllib.request
import os
import sys
import json

def call(keyword, start):
    client_id = "OXwS1xuacb66kX8AfAtY"
    client_secret = "NcNxkXMDw3"
    encText = urllib.parse.quote(keyword)
    url = "https://openapi.naver.com/v1/search/blog?display=100&start="+str(start)+"&query=" + encText  # json 결과
    # url = "https://openapi.naver.com/v1/search/blog.xml?query=" + encText # xml 결과
    resuslt = requests.get(url=url,
        headers= {"X-Naver-Client-Id":"OXwS1xuacb66kX8AfAtY",
                  "X-Naver-Client-Secret":"NcNxkXMDw3"})
    print(resuslt)
    return resuslt.json()

def get1000Result(keyword):
    list = []
    for num in range(0,10):
        list = list + call(keyword,num*100+1)['items']
    return list

#print(len(get1000Result("강남역맛집")))