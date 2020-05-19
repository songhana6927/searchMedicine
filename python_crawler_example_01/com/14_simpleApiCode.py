import requests
from urllib.parse import urlparse

keyword = "디퓨저"
url = "https://openapi.naver.com/v1/search/blog?query=" + keyword
result = requests.get(urlparse(url).geturl(),
                      headers={"X-Naver-Client-Id":"OXwS1xuacb66kX8AfAtY"
                          ,"X-Naver-Client-Secret":"NcNxkXMDw3"})
json_obj = result.json()
print(json_obj)
