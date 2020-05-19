import libs5.crawler as crawler

url = "https://news.naver.com/"
str = crawler.crawl(url)

print(str)