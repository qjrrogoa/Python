import numpy as np
import pandas as pd

#데이터프레임은 2차원 구조
#DataFrame 생성 첫번째 - 파이썬 딕셔너리
#{'키' : '값'}에서 '값'자리에 [] 리스트 형태로 입력
#키의 갯수는 열의 갯수가 되고 키값이 컬렴명이 된다.
#리스트의 요소들의 갯수는 각 행의 갯수가 된다.

dic = {'names':['가길동','나길동','다길동','라길동'],'score':[90,56,87,70],'grade':['A','F','B','C']}
df = pd.DataFrame(dic)
print(df)

#인덱스 지정하기
df = pd.DataFrame(dic,index=['FIRST','SECOND','THIRD','FOURTH'])
print(df)

#데이터 프레임의 인덱스와 컬럼에 이름 지정하기
print(df.index) #색인 인덱스 Index(['FIRST', 'SECOND', 'THIRD', 'FOURTH'], dtype='object')
print(df.columns) #컬럼 인덱스 Index(['names', 'score', 'grade'], dtype='object')
df.index.name='순서'
df.columns.name='컬럼명'
print(df)

#데이터 프레임의 주요 속성
'''
    DataFrame.index: 데이타 프레임의 색인(행 labels)을 반환한다
    DataFrame.values: 데이타 프레임의 NumPy 표현식으로 밸류값들을 반환한다
    DataFrame.dtypes: 데이타 프레임의 dtypes객체들을 반환							
    DataFrame.index.name:데이타 프레임 색인의 이름을 반환
    DataFrame.T :전치된 데이타 프레임를 반환(index와 column을 바꾼 형태)
    DataFrame.columns:데이타 프레임의 컬럼 labels를 반환
'''
print(df.index)
print(df.values) #2차원 넘파이 배열
print(df.dtypes)
print(df.columns)
print('[데이터 프레임의 전치 속성 T]')
print(df)
print(df.T)

#DataFrame 생성 두 번째 - columns인자로 키 값이 없는 컬럼 설정시
#columns의 리스트 요소는 딕셔너리의 키와 일치해야한다. 그렇지 않으면 각 행의 요소값이 NaN
df2 = pd.DataFrame(data=dic,index=['1st','2nd','3th','4th'],columns=['names','score','grade','years'])
print(df2) # years 칼럼추가되고 각 컬럼값은 NaN(Not a Number)

#DataFrame 생성 세번째 - 넘파이 배열
dates = pd.date_range('20210802',periods=4) #색인 인덱스 준비
print(dates)
arr = np.arange(1,13).reshape(4,3) #데이터 준비

df3 = pd.DataFrame(arr,index=dates,columns=list('가나다'))
print(df3)

#DataFrame 생성 네번째 - 파이썬 리스트
df4 = pd.DataFrame(data = [[1,2,3,4,5],[6,7,8,9,10]],columns=list('가나다라마'))
print(df4)