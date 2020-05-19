# 공공데이터 API 호출하기 - 부동산 실거래가
# https://www.data.go.kr/
# https://www.data.go.kr/dataset/3050988/openapi.do

## API 사용신청하기
# 사용신청을 해야 사용할 수있습니다.

# 시크릿키 발급받기
# 한입에 웹크롤링

import requests
from bs4 import BeautifulSoup
url = 'http://openapi.molit.go.kr/OpenAPI_ToolInstallPackage/service/rest/RTMSOBJSvc/getRTMSDataSvcNrgTrade'
queryParams = '?'+ 'LAWD_CD=' + '11110' \
              + '&DEAL_YMD=' + '202003' \
              + '&serviceKey=' + '4oroxVkY7KuoXOuq2PlApWDalcrygrZbmr2IrCJyhtm9gB0Q9l%2F%2FcBJYqkaNlm7d8p3kiUNA9P5t3J%2BpXEtPMg%3D%3D'

url = url+ queryParams

result = requests.get(url)
bs_obj = BeautifulSoup(result.content,"html.parser")
print(bs_obj)