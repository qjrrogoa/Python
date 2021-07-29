import numpy as np

nparr = np.arange(5)
print(nparr)
print('0번째 요소 :{},2번째 요소 :{},4번째 요소 :{}'.format(nparr[0],nparr[2],nparr[4]))
print(nparr[0],type(nparr[0]))
nparr[0] +=10;nparr[2] +=10;nparr[4] +=10;
print(nparr)

nparr2 = np.array(([[1,2,3,4,5],[6,7,8,9,10]]))
print(nparr2)

print('0행1열:{},1행2열:{}'.format(nparr2[0,1],nparr2[1,2]))
nparr3 = np.array([[[1,2,3],[4,5,6],[7,8,9]]])

'''
1:[#리스트라는 의미
   2:[
        3:[ 1  2  3]#axis 1에서 인덱스 0
        3:[ 4  5  6]#axis 1에서 인덱스 1
        3:[ 7  8 19]#axis 1에서 인덱스 2
    ]
]
1번 []는 리스트라는 의미
2번 []는 axis 가 0.  axis가 0인 대괄호가 하나임으로 인덱스는 0밖에 없다
3번 []는 axis 가 1.  axis가 1인 대괄호가 3개임으로 인덱스는 0,1,2
3번 []안의 요소 수가 axis가 2. 요소의 수가 3개임으로 인덱스는 0,1,2
'''
print(nparr3)
print('axis 0은 0,axis 1은 2,axis 2는 2:{}'.format(nparr3[0,2,2]))
nparr3[0,2,2]+=10
print('axis 0은 0,axis 1은 2,axis 2는 2:{}'.format(nparr3[0,2,2]))
'''
[시작인덱스:끝인덱스]사용하여 배열의 여러개 요소를 참조할때 사용하는 접근방법이 슬라이싱이다
            시작인덱스 생략시 0으로 처리되고
            끝인덱스 생략시 마지막 인덱스로 처리된다
            그래서 [:]는 전체 범위를 의미한다. 인덱스를 음수로 지정시에는 끝에서 시작하는 요소의 위치를 뜻한다
            즉 -1은 마지막 인덱스를 의미한다
'''
print(nparr[1:4])
print(nparr[:4])
print(nparr[1:])
print(nparr[:])
print(nparr[1:-1])

# 2차원 배열의 인덱스는 반드시 [  ,  ] 콤마를 기준으로
# 2개의 인자를 갖는다.첫번째 인자는 행의 인덱스를 의미
# 하고 두번째 인자는 열의 인덱스를 의미한다
# [행인덱스,열인덱스] 행인덱스와 열인덱스 두 곳에 : 이 포함되면 2차원 OUTPUT
#                    행인덱스와 열인덱스 둘 중 하나에 숫자 하나가 지정되면 1차원 OUTPUT
print(nparr2[1,1:4])
print(nparr2[1,:])
print(nparr2[:,1:4])
print(nparr2[0:-1,1:4])
print(nparr2[:,:])
#3차원 배열 슬라이싱
nparr3 = np.array(
    [
        [
            [1,2,3],
            [4,5,6]
        ],
        [
            [7,8,9],
            [10,11,12]
        ],
        [
            [13,14,15],
            [16,17,18]
        ]
    ]
)

print(nparr3.shape)
print(nparr3[1,:,0:2]) #차원 축소
print(nparr3[:-1,0:1,:])
#Numpy배열 요소 참조 - 불리언 인덱싱
#배열 요소의 선택여부를 True,False로 지정하는 방식으로 True에 해당하는 요소만 참조
scores = np.array(
    [
        [99,80,60],
        [78,90,90],
        [100,50,40]
    ]
)

students = np.array(['가길동','나길동','다길동'])
print(students == '나길동')
mask = students =='나길동'
print(mask.shape,mask.ndim,type(mask))
#이러한 마스크(불리언 배열)를 배열 슬라이싱 하는데 사용할 수 있다.
#즉 True 해당하는 열 혹은 슬라이싱 할 수 있다.
#나길동의 점수만 뽑아오자

nagildong = scores[mask,:]
print(nagildong) #행 인덱싱에 마스크 적용시 True인 행만 뽑는다.
print(nagildong,nagildong.shape)

#수학 점수가 90점 미만인 학생의 국영수 점수 뽑기
#1.마스크 생성
mask = scores[:,2] < 90
jumsu = scores[mask,:]
print(jumsu)