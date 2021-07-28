import numpy as np

#Numpy배열 생성하기 - 특정 조건ㅇ르ㅗ 데이터를 생성하는 함수
#0부터 10까지 5개를 균일한 간격으로 데이터를 생성하고 배열을 생
linspace=np.linspace(start=0,stop=10,num=5,endpoint=True)
print(linspace)
print('type : {}, shape : {}, dimension : {}, dtype : {} '.format(type(linspace),linspace.shape,linspace.ndim,linspace.dtype))
