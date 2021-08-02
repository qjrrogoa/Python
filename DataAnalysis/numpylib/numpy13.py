import numpy as np
#기타 넘파이 배열을 다루는 유용한 함수들

#np.copy(배열) 혹은 np.ndarray.copy()함수
arr = np.arange(1,11).reshape(5,2)
print(arr)

arr2 = np.copy(arr) #arr2 = arr.copy()
print(arr2)
arr2[:,1] = arr2[:,0]*10
print(arr2)

#배열을 axis(디폴트 값 : -1) 를 기준으로 배열요소를 정렬하는 함수
# np.sort(배열[,axis=-1]) 혹은 np.ndarray.sort([axis=-1])
np.random.seed(1)
arr3 = np.random.randint(1,12,(3,4))
print(arr3)
#arr3.sort(axis=0) #행측, 수직 방향, 요소가 재 배치된다.
#print(arr3)
arr3.sort(axis=1) #열측, 수평방향 정렬
print(arr3)

#배열의 중복되는 요소를 제외한 오름차순된 새로운 배열을 반환
#np.unique(ar[, return_index=False, return_inverse = False, return_counts=False, axis=None])
names = np.array(['나길동','가길동','홍길동','다길동','나길동','홍길동'])
names_unique = np.unique(names,return_index=True,return_counts=True)
print(names_unique)
print(names_unique[0])
print(names_unique[1])
print(names_unique[2])

#배열의 타입을 주어진 타입으로 변경한 새로운 배열 반환
print(arr.dtype)
arr_float = arr.astype(np.float64)