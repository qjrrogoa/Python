import numpy as np
#Numpy배열 생성하기 - array()함수
data1 = [1,2,3,4,5]
nparr1=np.array(data1)
print('type : {}, shape : {}, dimension : {}, dtype : {} '.format(type(nparr1),nparr1.shape,nparr1.ndim,nparr1.dtype))
print(nparr1) #[1,2,3,4,5] 콤마가 빠짐

data2 = [[1,2,3,4,5],[6,7,8,9,10]]#파이썬 2차원 리스트
nparr2 = np.array(data2)
print('type : {}, shape : {}, dimension : {}, dtype : {} '.format(type(nparr2),nparr2.shape,nparr2.ndim,nparr2.dtype))
print(nparr2)

data3 = [[[1,2,3],[4,5,6],[7,8,9]],[[10,11,12],[13,14,15],[16,17,18]]]#파이썬 3차원 리스트
nparr3 = np.array(data3)
print('type : {}, shape : {}, dimension : {}, dtype : {} '.format(type(nparr3),nparr3.shape,nparr3.ndim,nparr3.dtype))
print(nparr3)

#np.inf(infinity):무한대를 의미
#np.nan(not a number):정의할 수 없는 숫자
#예]1을 0으로 나누면 무한대 inf 그리고 0을 0으로 나누면 nan이 나온다.
np.seterr(divide='ignore',invalid='ignore')
nparr4 = np.array([1,0])/np.array([0,0])
print(nparr4)
#inf 및 nan을 넘파이 코드로
print('np.inf:{}, np.nan:{}'.format(np.inf,np.nan))
