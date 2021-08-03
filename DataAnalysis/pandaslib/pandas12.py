import numpy as np
import pandas as pd

#데이터 합치기
#concat() 함수 : 시리즈나 데이터프레임을 axis(디폴트 0)을 기준으로 하나로 합치는 함수
print('[시리즈 합치기]')
mans = pd.Series(['shirts','pants','jacket'])
print(mans)
womans = pd.Series(['blouse','knit'])
print(womans)
print(pd.concat([mans,womans])) #axis=0 디폴트(수직으로 결합 : 시리즈)
                                #axis=1 (수평으로 결합 : 데이터프레임)
'''
0    shirts
1     pants
2    jacket
0    blouse
1      knit
'''
print(pd.concat([mans,womans],ignore_index=True))
#ignore_index = True와 함께쓰면 keys는 무시되어 적용이 안된다.
#print(pd.concat([mans,womans],ignore_index=True),keys=['mans','womans']) #위와 같다
print(pd.concat([mans,womans],keys=['mans','womans']))
print(pd.concat([mans,womans],keys=['mans','womans'],names=['no','clothes']))#데이터 프레임처럼 생겼지만 시리즈다!!

print('[데이터프레임 합치기]')
df1 = pd.DataFrame([['가길동',80],['나길동',99],['다길동',80]],columns=['names','score'])
df1_ = pd.DataFrame([['라길동',70],['마길동',100]],columns=['names','score'])

print(pd.concat([df1,df1_],ignore_index=True))

df1__=pd.DataFrame([['라길동',70,'C'],['마길동',100,'A']],columns=['names','score','grade'])
print(pd.concat([df1,df1_,df1__],ignore_index=True)) #join = 'outer'디폴트 일치하는 컬럼이 없더라도 모두 합친다.
print(pd.concat([df1,df1_,df1__],ignore_index=True,join='inner'))#일치하는 컬럼인덱스만(axis=0) 가져온다.

df1___=pd.DataFrame([['컴퓨터공학',4],['산업공학',2]],columns=['major','years'])
print(pd.concat([df1,df1___],axis=1,join='inner')) #일치하는 행 인덱스만(axis=1) 합친다

#merge(함수)
df1 = pd.DataFrame({'lkey':['foo','bar','baz','foo'],'value':[1,2,3,5]})
df2 = pd.DataFrame({'rkey':['foo','bar','baz','foo'],'value':[5,6,7,8]})
print(df1)
print(df2)
print(df1.merge(df2))

print(df1.merge(df2,left_on='lkey',right_on='rkey'))
print(df1.merge(df2,left_on='lkey',right_on='rkey',suffixes=('_left','_right')))

#append()함수
dic ={
    'names':['가길동','나길동','다길동'],
    'years':[np.nan,np.nan,np.nan],
    'scores':[99,80,77],
    'grade':['A','B','C'],
    'major':[np.nan,np.nan,np.nan]}

df = pd.DataFrame(dic,index=list('가나다'))
print(df)
#데이터프레임 추가
df2=pd.DataFrame({
    'names': '가길동',
    'years': np.nan,
    'scores': 99,
    'grade': 'A',
    'major': np.nan}, index=['라'])
print(df2)
df3=df.append(df2,sort=True)
print(df3)

#df에 시리즈 데이터 추가
series = pd.Series(['바길동',4,60,'D','경영학'],index=df2.columns)
print(series)
print(df.append(series,ignore_index=True))