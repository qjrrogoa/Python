import numpy as np
import pandas as pd

#파일 읽기1
#csv파일의 헤더가 컬럼인덱스가 된다.
df = pd.read_csv('./data/titanic_train.csv')
print(df.head())
print(df.info())
#컬럼들 보기
print(df.columns)
print('[생존자만 보기]')
#생존자만 보기 : Survived == 1
#불리언 인덱싱 사용(df['Survived']==1) : query()함수 미사용
print(df[df['Survived']==1])
#query()함수 사용
print(df.query(expr='Survived==1')) #Where절과 같다

print('[NaN이 포함된 컬럼(Cabin)의 모든 값을 NaN으로 처리]')
#불리언 인덱싱 사용
df_ = df[df['Cabin'].isna()]
print(df_.info())
#query()함수 사용
df_=df.query(expr='Cabin.isnull()')
print(df_.info())

#파일 읽기 2
df1 = pd.read_csv('./data/titanic_train.csv',
                  skiprows=[0],
                  names=['승객번호','생사여부','좌성등급','이름','성별','나이','형제/자매/배우자 수','부모/자식 수','티켓번호','티켓요금','객실번호','승선항구'])
print(df1.head())
print(df1.columns)
print(df1['성별'].sample(10))
print('[성별이 female인 탑승객들 추출 : 불리언 인덱싱]')
print(df1[df1['성별']=='female']['성별'])
print('[성별이 female인 탑승객들 추출 : query()함수 사용')
#print(df1.query('성별 == "female"')['성별'])
print(df1.query('성별 == "female"').loc[:,'성별'])

#파일 읽기3
#index_col키워드 인수 : 특정 열의 데이터를 행 인덱스로 사용시
df2 = pd.read_csv('./data/titanic_train.csv',index_col='PassengerId')
print(df2.info())
print(df2.columns)

#파일 읽기 4
df3 = pd.read_csv('./data/blank.txt',names=['이름','나이','성별','거주지'],sep='\s+')
print(df3)

#파일 읽기 5
#na_values인수로 특정값을 NaN처리하기
df4 = pd.read_csv('./data/blank.txt',names=['이름','나이','성별','거주지'],sep='\s+',na_values=['나길동'])
print(df4)

#파일로 저장하기 - 데이터 프레임을 파일로 저장 : to_csv()함수
df.to_csv('./data/train_1.csv',index=False) #index = False로 행 인덱스 제외
#sep인수로 파일 저장시 구분자 바꾸기
df.to_csv('./data/train_2.csv',index=False,sep='|')
#na_rep인수로 NaN값을 특정 값으로 바꾸기
df.to_csv('./data/train_3.csv',index=False,sep='|',na_rep="결측치")
#header=False로 파일 저장시 컬럼 인덱스 제외
df.to_csv('./data/train_4.csv',index=False,sep='|',na_rep="결측치",header=False)

