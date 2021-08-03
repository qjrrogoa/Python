import numpy as np
import pandas as pd
import datetime

np.random.seed(0)
#시계열 데이터 : 행인덱스가 날짜나 시간인 데이터
#DatetimeIndex 인덱스 생성하기 : to_datetime()함수

dates = ['2021, 1, 1',np.datetime64('2021-01-02'),'2021/1/3',datetime.datetime(2021,1,4)]
index = pd.to_datetime(dates)
print(index) #DatetimeIndex

#시계열 인덱스를 사용해서 시계열 데이터(데이터 프레임) 생성
data = [[900,2000,1000,900],[1500,2500,900,1500],[1000,2800,1500,2000],[7000,8000,75000,6000]]
df = pd.DataFrame(data,index=index,columns=['Open','High','Low','Close'])
print(df)

#DatatimeIndex 인덱스 생성하기 : date_range()함수
#index = pd.date_range('2021/1/1','2021/1/4') #freq디폴트는 'D'
index = pd.date_range('2021/1/1',periods=4)
#index = pd.date_range('2021/1/1',periods=4,freq='3MS')
print(index)
df = pd.DataFrame(data,index=index,columns=['Open','High','Low','Close'])
print(df)

#시계열 데이터 관련 유용한 함수 : shift()함수
print(df.shift(periods=2)) #시계열순으로 2만큼 데이터가 이동하고 빈 자리는 NaN으로 채워짐
print(df.shift(fill_value=0)) #periods=1이 티폴트, Nan을 0으로 채움

#시계열 데이터 관련 유용한 함수 : resample()함수
ts = pd.Series(np.random.randn(100),index=pd.date_range('2021-1-1',periods=100))
print(ts.tail(10))

#일을 월로 인덱스를 리샘플링 : 다운 샘플링(100개의 일 데이터가 4개의 월데이터로 다운)
#1.1~1.31까지의 시계열 데이터는 1월로 그룹핑
#그룹바이때와 같이 집합연산(max(),min(),sum()등)을 해서 대표값을 구해야 한다.
print(ts.resample(rule='MS').max())

ts = pd.Series(np.random.randn(60),index=pd.date_range('2021-1-1',periods=60,freq='min'))
print(ts.head())
print(ts.resample(rule='10min').sum())

#ohlc메서드는 구간의 시고저종(open,high,low,close)값을 구한다.
print(ts.resample(rule='5min').ohlc())

#업샘플링 : 1분단위를 30초단위로 리샘플링
'''
업-샘플링의 경우에는 실제로 존재하지 않는 데이터를 만들어야한다.
이 때는 앞에서 나온 데이터를 뒤에서 그대로 쓰는 ffill 메서드와
뒤에서 나올 데이터를 앞에서 미리 쓰는 btill메서드를 이용한다.
'''
print("원본 데이터")
print(ts.head(20))
print("업 샘플링한 데이터")
print(ts.resample('30s').ffill().head(20)) #과거 데이터
print(ts.resample('30s').bfill().head(20)) #최근 데이터
