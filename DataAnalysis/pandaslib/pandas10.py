import numpy as np
import pandas as pd

data = [[1,2,np.nan],[4,5,6],[7,np.nan,np.nan],[10,11,12]]
df = pd.DataFrame(data,columns=list('ABC'),index=list('가나다라'))
print(df)

#수학 및 통계학적 연산
#기본적으로 NaN는 제외시킨다. NaN을 포함시키려면
#skipna = False
#describe()함수 : 각 열(행방향)의 수치에 대한 요약 통계
print(df.describe()) #include = 'all'는 object컬럼 포함

#count()함수
print(df.count())
print(df.count(axis=1))

#min()함수
print(df.min(numeric_only=True,axis=1))

#max()함수
print(df.max(numeric_only=True,axis=1,skipna=False))

#idxmax()함수
print(df.idxmax()) #각 열의 최대값이 있는 행 인덱스 반환
print(df.idxmin()) #각 열의 최소값이 있는 행 인덱스 반환

#sum()함수 : axis=0
print(df.sum()) #각 열의 합

#B열의 총합
print(df['B'].sum())

#나행의 총합
print(df.loc['나'].sum())

#mean()함수
print(df.mean()) #각 열의 평균
print(df.mean(axis=1))

#median()함수
print(df.median())#각 열의 중앙값


