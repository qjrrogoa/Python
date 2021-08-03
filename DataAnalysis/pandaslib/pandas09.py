import numpy as np
import pandas as pd

#산술 연산
df = pd.DataFrame({'angles':[0,3,4],'degrees':[360,180,360]},index=['circle','triangle','rectangle'])
print(df)

print(df.add(1)) #df+1
print(df.sub(1)) #df-1
print(df.mul(10)) #df*10
print(df.div(10)) #df/10
print(df.mod(10)) #df%10

print(df.sub([1,2,3],axis=0))
print(df.sub([1,2],axis=1))

#Series
#산술연산에서 시리즈를 사용할 경우, 인덱스를 DF과 똑같이 만들어줘야한다.
#series = pd.Series([1,2,3],index=['circle','triangle','rectangle'])
series = pd.Series([1,2,3],index=df.index)
print(series)
print(df.sub(series,axis=0))

df2 = pd.DataFrame({'angles':[0,3,4]},index=df.index)
print(df2)
#df2의 없는 컬럼인 degrees의 값을 100으로 설정 후 빼기한다.
print(df.sub(df2,fill_value=100))
print(df.mul(df2))

#apply() 함수 : 데이터프레임의 각 요소값에 기존 존재하는 함수를 적용한거나 사용자가 정의한
#(람다)함수를 적용하여 각 요소를 변형하고자 할 때 사용.
#함수는 인자를 하나만 받는 함수여야한다(데이터 프레임의 각 요소가 하나씩 전달됨으로)
df3 = pd.DataFrame([[4,9]] * 3,columns=['A','B']) # 3X2 데이터 프레임
print(df3)
print(df3.apply(pd.isna))
print(df3 == np.isnan) #위와 같다
print(df3.apply(np.sum)) #axis=0이 디폴트
print(df3.apply(np.sum,axis=1))

print(df3.apply(lambda x:[1,2],axis=1))
#리스트를 반환하는 함수를 인자로 준 경우 reesult_type = 'expand'를 주면 데이터프레임된다
#아래 컬럼인덱스는 리스트의 요소수만큼 정수인덱스가 된다.
print(df3.apply(lambda x:[1,2],axis=1,result_type='expand')) #데이터프레임. 리스트의 각 요소가 데이터프레임의 요소가 된다.
print(df3.apply(lambda x:[1,2],axis=1,result_type='broadcast')) #데이터프레임. 컬럼명이 원본 컬럼인덱스가 된다.

df3 = pd.DataFrame([[4,5,9],[7,8,10]])
def myfunc(x):
    return x % 3
print(df3.apply(myfunc))