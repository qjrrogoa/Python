import numpy as np
#Numpy배열 변경하기 2
#append함수
#배열의 끝에 값을 추가하는 함수.
#axis로 값이 추가되는 방향을 설정할 수 있다.
#axis를 지정하지 않으면 1차원 배열로 변경되어 추가
np.random.seed(1004)
arr1 = np.random.randint(1,10,size=(3,4)) #10포함 안된다
print(arr1)

arr2=np.random.randint(1,10,size=(3,4))
print(arr2)

#axis를 지정하지 않는 경우 : 1차원 배열로 변경
print(np.append(arr1,99))#스칼라 추가
print(np.append(arr1,values=arr2))

#axis를 지정한 경우
#np.append(arr1,values=99,axis=0) #axi지정시에는 스칼라 추가 불가
print(np.append(arr1,arr2,axis=0)) #arr1에 수직으로 행이 추가됨
print(np.append(arr1,arr2,axis=1)) #arr1에 수직으로 행이 추가됨

print(np.append(arr1,arr2,axis=0))#열의 수가 같아야한다. arr1에 수직으로 행이 추가됨
#arr2를 4행 4열로 변경
arr2.resize((3,4),refcheck=False)
print(arr2)
print(np.append(arr1,arr2,axis=1))#행의 수가 같아야 한다. arr1에 수평으로 열이 추가됨

#insert함수
arr3 = np.arange(1,13).reshape(3,4)
print(arr3)
#axis지정 안하고 스칼라 값 insert:1차원으로 변경되서 insert
print(np.insert(arr3,obj=7,values=77))

#axis지정
print('[axis=0]')
print(np.insert(arr3,obj=1,values=100,axis=0))
print(np.insert(arr3,obj=1,values=[1,2,3,4],axis=0))

print('[axis=1]')
print(np.insert(arr3,obj=2,values=100,axis=1))
print(np.insert(arr3,obj=2,values=[1,2,3],axis=1))

#delete함수
print(arr3)

#axis 미 지정
print(np.delete(arr3,[2,4,10]))#1차원으로 변경 된 후 인덱스가 2,4,10째 자리 삭제

#axis 지정
print(np.delete(arr3,[0,2],axis=0))
print(np.delete(arr3,[0,2],axis=1))