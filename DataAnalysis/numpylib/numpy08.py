import numpy as np
#산술연산
arr1 = np.array(
    [
        [1,2,3],
        [4,5,6]
    ]
)

arr2 = np.array(
    [
        [7,8,9],
        [10,11,12]
    ]
)

#덧셈
print(arr1+arr2)
print(np.add(arr1,arr2))

#뺄셈
print(arr1-arr2)
print(np.subtract(arr1,arr2))

#나눗셈
print(arr1/arr2)
print(np.divide(arr1,arr2))

#나머지
print(arr1%arr2)
#요소 별 몫과 나머지를 동시에 반환
#0번째 요소는 몫, 1 인덱스 요소는 나머지
#즉 [1]로 인덱싱
print(np.divmod(arr1,arr2)[1])

#비교연산
#짝수인 요소를 모두 100으로 변경
#[불리언 배열(마스크)]시 True에 해당하는 요소를 참조할 수 있다.
print(arr1[arr1 % 2 == 0])#[2,4,6]
arr1[arr1 % 2==0]=100
print(arr1)

arr2[arr2 % 2==0]=100
print(arr2)

print(np.array_equal(arr1,arr2)) #먼저 shape 부터 비교 다르면 False,같으면 다시 요소의 값비교 모든 요소가 같으면 True 다르면 False


# 수학 및 통계적인 연산 - 어떤 axis를 연산시 차원축소
print(np.sum(np.arange(1,11)))
arr1=np.arange(1,11).reshape(5,2)
print(arr1)
print(np.sum(arr1)) #55,axis를 지정하지 않으면 모든 행,열 요소 값 다 더한다.
print(arr1.sum()) #55
print(np.sum(arr1,axis=0)) # 각 열들의 합을 구향(행 방향) [25,30]
print(np.sum(arr1,axis=1)) # 각 행들의 합을 구향(열 방향) [ 3  7 11 15 19]

# 불리언 배열(마스크)을 만든 후
# sum()함수를 적용하면 True는 1로, False는 0으로 계산되서 합계됨
# 짝수의 갯수를 알아내자
mask = arr1 % 2 == 0
print(mask)
print('짝수의 개수 : ',np.sum(mask))

# 최대 값
print(np.max(arr1))#혹은 arr1.max() 모든 요소에서 최대값 반환
print(np.max(arr1,axis=0)) #[ 9 10]
print(np.max(arr1,axis=1)) #[ 2  4  6  8 10]

# 최소 값
print(np.min(arr1))#혹은 arr1.max() 모든 요소에서 최대값 반환
print(np.min(arr1,axis=0)) #[1 2]
print(np.min(arr1,axis=1)) #[1 3 5 7 9]

# 평균 값
print(np.mean(arr1))#혹은 arr1.max() 모든 요소에서 최대값 반환
print(np.mean(arr1,axis=0)) #[5. 6.]
print(np.mean(arr1,axis=1)) #[1.5 3.5 5.5 7.5 9.5]

# 누적 값
#차원 축소
print(np.cumsum(arr1))
#아래는 shape이 그대로 유지
print(np.cumsum(arr1,axis=0))
print(np.cumsum(arr1,axis=1))

#shape이 다른 배열들의 아항 연산 : 브로드 캐스팅
arr1 = np.array([[0],[10],[20],[30]])
print(arr1.shape)#4X1
arr2 = np.array([[0,1,2]])
print(arr2.shape)#1X3
print(arr1+arr2)
print((arr1+arr2).shape) #4X3