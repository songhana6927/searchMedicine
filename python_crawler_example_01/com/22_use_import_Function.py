from libs5.naver_api_caller import get1000Result
import json

#json 검색결과 파일로 저장

result = get1000Result("강남역 맛집")
result2 = get1000Result("강남역 찻집")
list = result + result2

#print(list)

file = open("./gangnam.json","w+")
file.write(json.dumps(list))