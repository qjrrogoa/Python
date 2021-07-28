import numpy as np
#리스트는 모든 타입을 요소로 가질 수 있다.
data = ['HELLO',100,3.14,True]

#파이썬 리스트나 튜플로 NumPy배열 만들기 - np.array(파이썬 리스트나 혹은 튜플)함수 사용
print(np.array(data))
print(type(np.array(data)))#<class 'numpy.ndarray'>

#같은 타입의 데이터를 가진 리스트나 튜플로 NumPy배열 만드기
nparr = np.array([i for i in range(1,6)])
print ('nparr : {}, type : {}'.format(nparr,type(nparr)))
for e in nparr:
    print(e,type(e))

#튜플로 넘파이 배열 생성
nparr2 = np.array(('A','B','C','D','E'))
print ('nparr2 : {}, type : {}'.format(nparr2,type(nparr2 )))
