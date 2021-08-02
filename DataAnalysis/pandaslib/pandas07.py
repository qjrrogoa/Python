import numpy as np
import pandas as pd
df = pd.DataFrame(np.random.rand(5,5))
print(df)
#데이터 프레임의 정수인덱스는 타입이 RangeIndex(시리즈는 Index)
print(df.index) #RangeIndex(start=0, stop=5, step=1)
print(df.columns) #RangeIndex(start=0, stop=5, step=1)
df.columns=list('가나다라마')#컬럼 인덱스 변경
print(df)
df.index=pd.date_range('20210617',periods=5) #행 인덱스 변경
print(df)

#결측치 관련 함수들
#dropna()함수
#결측치가 존재하는 행을 제외
#how='any' : 행의 각 컬럼에 NaN이 하나라도 있으면 그 행을 제거
#how='all' : 행의 모든 칼럼이 모두 NaN일때 그 행을 제거
#axis=0 디폴트 즉 행 제거 열 제거시에는 axis=1
df['바'] =[0.5,np.nan,1.0,np.nan,100]
#print(df.dropna(inplace=True)) #not in-place
print(df.dropna(how='all')) #행 제거 안된다
print(df.dropna(how='any',axis=1)) #열 제거 된다
print(df)

#fillna()함수 : 결측치가 있는 부분을 다른 값으로 채우는 함수
print(df.fillna(0.1))

#isna()함수 혹은 insull()함수 : 결측치에 해당하면 True,아니면 False로 불린 마스크를 생성하는 함수
print(df.isna())
print(df.isnull())

#불리언 마스크를 사용해서 바열에서 NaN인 행만 모두 가져오기
mask = df.isnull()
print(mask['바'])
print(df.loc[mask['바'],:])

#'바'열에서 100이 포함된 행을 제거하시오 즉 21일 행이 제거되야 한다.
#NaN을 먼저 임의의 값으로 설정
df.fillna(0.5,inplace=True)
#2. 데이터 프레임의 값 모든 요소 비교
mask = df < 100
print(df.loc[mask['바'],:])
