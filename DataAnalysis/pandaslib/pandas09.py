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