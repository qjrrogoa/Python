import numpy as np
import pandas as pd

columns = list('가나다라마') #list타입
index = pd.date_range('2021-1-1',periods=5) #DatetimeIndex타입
df = pd.DataFrame(np.random.rand(5,5),index=index,columns=columns)
print(df)
'''
shuffle과 permutation함수
- 배열의 요소를 무작위로 섞는 함수
- 차이점
 shuffle은 in-place방식
 permutation은 새로운 배열 반환(not in-place방식)
'''
arr = np.arange(10)
print(arr)
np.random.shuffle(arr)
print(arr)
print(np.random.permutation(arr))
print(arr)

#RangeIndex나 DatetimeIndex등은 immutable하다
#shuffle사용시 에러 : index는 mutation operation을 지원 안함
#인덱스는 mutable연산 불가 즉 permutation()함수를 적용해야한다.
random_index = np.random.permutation(index)
#random_index = np.random.shuffle(index) #TypeError
print(random_index)

np.random.shuffle(columns)
print(columns)

#무작위로 섞은 인덱스와 컬러명으로 데이터프레임 또 생성
df2 = df.reindex(index=random_index,columns=columns)
print("=========재색인 전==========")
print(df)
print("=========재색인 후==========")
print(df2)

#인덱스 기준 정렬
#행 방향으로 인덱스를 오름차순 정렬
print(df2.sort_index())
#열 방향으로 인덱스를 오름차순 정렬
print(df2.sort_index(axis=1))

#행 방향으로 인덱스를 내림차순 정렬
print(df2.sort_index(ascending=False))
#열 방향으로 인덱스를 내림차순 정렬
print(df2.sort_index(axis=1,ascending=False))

#데이터 기준으로 정렬
print(df2.sort_values(by='가'))
print(df2.sort_values(by='가',ascending=False))
print(df2.sort_values(by=np.datetime64('2021-01-01'),axis=1))
print(df2.sort_values(by=np.datetime64('2021-01-01'),axis=1,ascending=False))
print(df2.sort_index(axis=1).sort_values(by=['가','나'],ascending=False))


