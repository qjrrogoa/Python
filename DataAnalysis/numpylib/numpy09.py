import numpy as np
#Numpy 배열 변경하기 1
#shape변환

arr= np.arange(1,13,dtype=np.float64)
print(arr)
print('shape : {}, dimension : {}'.format(arr.shape,arr.ndim)) #shape : (12,), dimension : 1

#reshape함수
arr_reshape = arr.reshape((4,3))
print('shape : {}, dimension : {}'.format(arr_reshape.shape,arr_reshape.ndim)) #shape : (12,), dimension : 1
print(arr_reshape)

#resize함수 : shape을 변경 및 요소의 크기 resize
#np.resize(넘파이 배열, 새로운 shape) : not in-place
arr_resize=np.resize(arr,new_shape=(3,4))
print(arr_resize)
print(arr)
#ndarray.resize(새로운 shape) : in-place

#요소수 늘이기
arr_resize_increase=np.resize(arr,(5,4))
print(arr_resize_increase) #기존 배열이 행 또는 열축으로 쌓인다.
arr_resize_increase=arr.resize((6,4),refcheck=False) #반환값이 없다
                                                    #추가된 행이나 열이 해당 배열의 dtpye의 기본값으로 채워진다.
print(arr_resize_increase) #None
print('[ndarray.resize]')
print(arr)

#요소수 줄이기
arr= np.arange(1,13,dtype=np.float64)
print(arr)
print(np.resize(arr,(2,3)))
print('[ndarray.resize:요소수 줄이기')
print(arr.resize((2,3),refcheck=False))
print(arr)

#ravel함수
print(arr.ravel()) #배열의 shape를 1차원 배열로 변경 not in-place
print(arr)

