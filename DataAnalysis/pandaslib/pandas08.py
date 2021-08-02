import numpy as np
import pandas as pd
index = ['Firefox','Chrome','Safari','Edge','Opera']
dic={'status_code':[200,200,404,404,301],'response_time':[0.04,0.02,0.07,0.08,1.0]}
df = pd.DataFrame(data=dic,index=index)
print(df)

#데이터를 새로운 인덱스에 맞게 재배열, 없는 인덱스 값이 있다면 비어있는 값(NaN)을 새로 추가
#재색인
new_index=['Safari','Iceweasel','Comodo Dragon','Edge','Chrome']
#print(df.reindex(new_index))
#fill_value인자 : 결측치 대체하기
#추가된 새로운 색인에 대한 결측치 값들을 지정한 값으로 채운다.
print(df.reindex(new_index,fill_value=0))

#칼럼이 바뀜
print(df.reindex(columns=['status_code','user_agent']))
print(df.reindex(labels=['status_code','user_agent'],axis='columns')) #위랑 똑같다

#행이 바뀜
print(df.reindex(['status_code','user_agent']))
print(df.reindex(labels=['status_code','user_agent'],axis='index')) #위랑 똑같다

#reindex랑 index는 완전 다르다
#df.index = ['status_code','user_agent','a','b','c'] #행의수와 일치해야되고 일치시는 에러는 나지않으나 요소의 값이 그대로 적용된다.
#print(df)

print(df.reindex(new_index,columns=['status_code','user_agent']))#동시에 행인덱스와 컬럼인덱스 변경
#시계열 데이터 재색인하기
date_index = pd.date_range('8/2/2021',periods=6,freq='D')
print(date_index)

df2 = pd.DataFrame({'price':[100,101,np.nan,100,89,88]},index=date_index)
print(df2)

date_index2 = pd.date_range('7/30/2021',periods=12)
#print(df2.reindex(date_index2))
print(df2.reindex(date_index2,method='ffill'))
print(df2)

#행 삭제하기
#하나의 행 삭제 하기
#drop하고자 하는 행 인덱스명, 열인덱스명을 스칼라나, 리스트로 입력하며
# axis= 1 일 경우 열을 drop(axis=0이 디폴트)
#print(df2.drop('2021-08-03'))
print(df2.index)
print(df2.drop(np.datetime64('2021-08-03'))) #df2.drop('2021-08-03')에러시 datetime

#여러행 삭제하기
print(df2.drop(['2021-08-02','2021-08-06']))


#열 삭제하기
df2['income']=np.random.randint(4000,5000,6)
df2['loss']=np.random.randint(-100,-50,6)
print(df2)

#하나의 열 삭제
print(df2.drop('price',axis=1)) #not in-place
#del df2['price'] #in-place

#여러열 삭제
print(df2.drop(['income','loss'],axis=1))
print(df2.drop(['income','loss'],axis=1).dropna())
