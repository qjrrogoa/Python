import numpy as np
#Numpy배열 파일 입출
arr=np.loadtxt('./data/sample.csv',delimiter=',') #디폴트 데이터 타입은 float
print(arr)
print(type(arr))

#loadtxt 함수 두번째
#방법1
#arr=np.loadtxt('./data/sample2.csv',delimiter=',',skiprows=1,encoding='utf-8',dtype=str) #디폴트 데이터 타입은 float

#방법2
#arr=np.genfromtxt('./data/sample2.csv',delimiter=',',encoding='utf-8',skip_header=1,dtype='str')
print(arr)
print(type(arr))

#방법3
import pandas as pd
df=pd.read_csv('./data/sample2.csv',sep=',',encoding='utf-8',skiprows=0)
print(df)
arr=np.array(df) #데이터 프레임을 넘파이 배열로 변환
print(arr)
print(type(arr))

#NumPy배열을 텍스트 파일로 저장.
#savetxt()함수
arr2 = np.arange(1,11).reshape((2,5))
#fmt는 파일저장시 포맷
np.savetxt('./data/save.csv',arr2,fmt='%d',delimiter=',')
np.savetxt('./data/save2.csv',arr,fmt='%d,%s,%s,%s',delimiter=',',encoding='utf-8')
