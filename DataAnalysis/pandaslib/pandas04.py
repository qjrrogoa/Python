import numpy as np
import pandas as pd

#데이터 프레임 참조하기 2
dic = {'names':['가길동','나길동','다길동','라길동'],'score':[90,56,87,70],'grade':['A','F','B','C']}
df = pd.DataFrame(dic,columns=['names','years','score','grade','major'],index=list('가나다라'))
print(df)

# 정수인덱스든 행인덱스명이든 항상 :이 포함되어야한다. df[ : ]
#행 가져오기 - 슬라이싱
#print(df['가']) #KeyError : 열 인덱스 컬럼명에서 '가'를 찾는다
print(df['가':'나'])

#정수 인덱스로 여러행 가져오기
#df[정수시작 행 인덱스 : 정수끝 행 인덱스] 이때 정수 끝 인덱스는 포함 안됨
#print(df[1]) #KeyError : 열 인덱스 컬럼명에서 1를 찾는다
print(df[1:2])
print(df[0:2])

#행 인덱스명으로 여러행 가져오기
#df['시작인덱스명':'끝인덱스명'] 이때는 끝인덱스명도 포함됨
#print(df['가':'나'])
#print(df['다':'가']) #Empty DataFrame 인덱스 순서대로 슬라이싱해야 한다.
