import numpy as np
# Numpy배열 생성하기 - 특정값으로 초기화 하는 함수
# 모든 요소를 0으로 초기화. 데이터 타입 디폴트는 np.float64

zeros = np.zeros(shape=(5,)) #np.zeros(5)
print(zeros)
print('type : {}, shape : {}, dimension : {}, dtype : {} '.format(type(zeros),zeros.shape,zeros.ndim,zeros.dtype))

#인자로 주어진 배열과 같은 shape와 dtype 및 ndim을
#가진 배열을 생성하고 모든 요소를 0으로 초기화
zeros = np.zeros_like(np.array([[1,2,3,],[4,5,6]]))
print(zeros)
print('type : {}, shape : {}, dimension : {}, dtype : {} '.format(type(zeros),zeros.shape,zeros.ndim,zeros.dtype))

#모든 요소를 1로 초기화, 데이터 타입 디폴트는 np.float64
ones = np.ones((5,))
print(ones)
print('type : {}, shape : {}, dimension : {}, dtype : {} '.format(type(ones),ones.shape,ones.ndim,ones.dtype))

#인자로 주어진 배열과 같은 shape와 dtype 및 ndim을
#가진 배열을 생성하고 모든 요소를 1로 초기화
ones = np.ones_like(np.array([[1,2,3],[4,5,6]]))
print(ones)
print('type : {}, shape : {}, dimension : {}, dtype : {} '.format(type(ones),ones.shape,ones.ndim,ones.dtype))

#주어진 shape의 배열을 생성하고 모든 요소를 지정한 "fill_value"로 초기화
full = np.full(shape=(2,3),fill_value=10,dtype=np.float32)
print(full)
print('type : {}, shape : {}, dimension : {}, dtype : {} '.format(type(full),full.shape,full.ndim,full.dtype))

# 임의의 값을 가진 넘파이 배열이 생성
# 데이터 타입 디폴트는 np.float64
empty = np.empty(shape=(3,3))
print(empty)

