import numpy as np

#Numpy배열 생성하기 - 특정 조건ㅇ르ㅗ 데이터를 생성하는 함수
#0부터 10까지 5개를 균일한 간격으로 데이터를 생성하고 배열을 생
linspace=np.linspace(start=0,stop=10,num=5,endpoint=True)
print(linspace)
print('type : {}, shape : {}, dimension : {}, dtype : {} '.format(type(linspace),linspace.shape,linspace.ndim,linspace.dtype))

#균일한 간격을 직접 지정
#start 디폴트는 0
#step 디폴트는 1
arange = np.arange(start=0,stop=10,step=3,dtype=np.float32)
print(arange)
print('type : {}, shape : {}, dimension : {}, dtype : {} '.format(type(arange),arange.shape,arange.ndim,arange.dtype))

#arange()는 ndarray객체, 파이썬의 range객체와 같다(range객체)
print(np.arange(5))
print(np.array([ i for i in range(5)]))

logspace = np.logspace(start=0.1,stop=1,endpoint=False,num=10)
print(logspace)
import matplotlib.pyplot as plt
plt.plot(logspace,'r--')
plt.show()