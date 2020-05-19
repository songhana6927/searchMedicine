# Python Pandas 로 데이터 분석하기
# 600개 리스트 에 제일 많이나온 블로거 이름 찾기

import pandas as pd


df = pd.read_json("./gangnam.json")
# 필드당 카운트
# print(df.count())

# 블로그 그룹바이 카운트
# dfSum = df.groupby("bloggername").count()
# print(dfSum)

# # 원하는 필드만 뽑기
# bloggernames = df['bloggername']
# print(bloggernames)