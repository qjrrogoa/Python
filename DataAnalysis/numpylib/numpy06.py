import numpy as np
import matplotlib.pyplot as plt
#Numpy배열 생성하기 - 랜덤한 배열 생성
#loc는 평균, scale = 표준편차
normal = np.random.normal(loc=0,scale=1,size=100)
print(normal)
print('type : {}, shape : {}, dimension : {}, dtype : {} '.format(type(normal),normal.shape,normal.ndim,normal.dtype))
'''
plt.hist(normal)
plt.show()
'''

#0과 1의 범위 균등분포에서 랜덤한 값으로 초기화 된 shape가 (5,2)배열 생성 유니폼분포
rand = np.random.rand(5,2)
print(rand)
print('type : {}, shape : {}, dimension : {}, dtype : {} '.format(type(rand),rand.shape,rand.ndim,rand.dtype))
'''
plt.hist(rand)
plt.show()
'''

#5부터 10미만 범위에서 정수를 추출하여 size(shape)형태로 배열 생성
randint =  np.random.randint(low=5,high=10,size=(5,2))
print(randint)
print('type : {}, shape : {}, dimension : {}, dtype : {} '.format(type(randint),randint.shape,randint.ndim,randint.dtype))

random = np.random.random(size=(5,2))
print(random)
