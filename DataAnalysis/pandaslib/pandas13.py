import numpy as np
import pandas as pd

#데이터 그룹화 하기
np.random.seed(0)
df = pd.DataFrame({
    'A':['foo','bar','foo','bar','foo','bar','foo','foo'],
    'B':['one','one','two','three','two','two','one','three'],
    'C':np.random.randint(1,8,8),
    'D':np.random.randint(1,8,8)})
print(df)

#단일 함수(집합함수 혹은 그룹함수)를 사용하여 GroupBy집계
grouped = df.groupby('A') #A컬럼을 기준으로 그룹핑 group by 컬럼명과 같다
print(grouped) #DataFrameGroupBy object
print(dir(grouped))
print(grouped.sum()) #select sum('모든 숫자 컬럼')
#2 혹은 DataFrameGroupBy객체.agg('함수명')
print(grouped.agg('sum'))
#
print(df.groupby('A').max())
print(df.groupby('A').agg('max'))
#sort=False 인자로 그룹핑 속도를 높일 수 있다
print(df.groupby('A',sort=False).agg('min'))
#여러 컬럼을 기준으로 그룹핑하여 집계
print(df.groupby(['A','B']).max())
print(df.groupby(['A','B']).agg(['sum','mean','min','max','size','count']))
#agg({})
print(df.groupby(['A','B']).agg({'C':['sum','mean'],'D':['min','max']}))

#('별칭명','함수명')
print(df.groupby(['A','B']).agg({'C':[('합계','sum'),('평균','mean')],'D':[('그룹수','size')]}))


