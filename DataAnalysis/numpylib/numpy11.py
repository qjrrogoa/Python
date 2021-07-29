import numpy as np
#Numpy배열 변경하기3
#concatenate함수
arr1 = np.arange(1,11).reshape(2,5)
print(arr1)
arr2 = np.arange(11,21).reshape(2,5)
print(arr2)

#axis 미지정
print(np.concatenate((arr1,arr2)))        #행방향으로 결합

#axis 지정
print(np.concatenate((arr1,arr2),axis=0)) #미지정과 같다
print(np.vstack((arr1,arr2)))             #위와 같다 행으로 쌓기
print(np.concatenate((arr1,arr2),axis=1)) #미지정과 같다
print(np.hstack((arr1,arr2)))             #위와 같다 열로 쌓기

#hsplit 함수

arr3 = np.arange(0,30).reshape(5,6)
print(arr3)

print(np.hsplit(arr3,2)) # 두번째 인자는 분리할 배열의
                         # 분리된 배열의 차우너은 모두 동일해야 한다
                         # h는 수평 즉 열방향으로 분리된다

arr3_hsplit=np.hsplit(arr3,2)
print(arr3_hsplit[0])

print(np.vsplit(arr3,5))
print(np.vsplit(arr3,5)[0])

print(np.hsplit(arr3,[1,3,5])) #[:,:1] 배열 하나, [:,1:3] 배열 하나, [:,3:5] 배열 하나, [:,5:]배열 하나

print(np.vsplit(arr3,[1,3])) # [:1,:] 배열 하나, [1:3,:] 배열 하나, [3:,:] 배열 하나


#전치)Transepose)사용
print(arr1)
print(arr1.T)
