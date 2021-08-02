import numpy as np
import pandas as pd

#시리즈는 1차원 구조
#Series생성 첫번째 - 파이썬 리스트
series = pd.Series([90,85,60,55,70]) #index 미 지정시에는 기본적으로 정수 인덱스가 지정
print(series)

series = pd.Series([90,85,60,55,70],index=['A','B','D','F','C']) #index = []형태로 설정
print(series)

series = pd.Series([90,85,60,55,70],index=['A','B','D','F','C'],name='학점')
print(series)

#시리즈의 주요 속성
print(series.index) # Index(['A', 'B', 'D', 'F', 'C'], dtype='object')
print(type(series.index)) # <class 'pandas.core.indexes.base.Index'>
print(series.name) # 학점 미 지정시 None
print(series.values) # [90 85 60 55 70] Numpy배열
print(type(series.values))# <class 'numpy.ndarray'>
print(series.dtype) # int64

#색인에 대한 이름 지정
series.index.name='등급'
print(series)

#Series생성 두번째 - 파이선 딕셔너리
series2 = pd.Series({'A':90,'B':85,'D':60,'F':55,'C':70})
print(series2) #딕셔너리의 키가 인덱스(색인)가 된다
series2.name = '학점' #시리즈 이름
series2.index.name = '등급' #색인 이름
print(series2)
print(series2.index)
series2.index=['A학점','B학점','D학점','F학점','C학점'] #각 인덱스의 이름 변경하기
print(series2)


#Series생성 세번째 - 넘파이 배열(#반드시 1차원형태의 자료구조여야 한다.)
series3 = pd.Series(np.arange(1,13))
#series3 = pd.Series(np.arange(1,13).reshape(3,4)) 오류 쫙 난다
print(series3)

