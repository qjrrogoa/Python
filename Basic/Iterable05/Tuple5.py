print('[2차원 튜플]')
#바깥쪽 ()는 튜플을 의미
#안쪽 ()의 수: 행의 수
#안쪽 ()의 값(요소)의 수 :열의 수
a=(
    (1,2),
    (3,4),
    (5,6)
)#3행 2열 리스트
print('value:{},type:{}'.format(a,type(a)))
#행의 수: len(튜플객체)
#열의 수: len(튜플객체[행인덱스])
print('행의 수:',len(a))
print('0행의 열의 수:',len(a[0]))
print('1행의 열의 수:',len(a[1]))
print('2행의 열의 수:',len(a[2]))
print('[2차원 튜플의 각 요소 읽기]')
print('0행0열:',a[0][0])
print('0행1열:',a[0][1])
print('2행0열:',a[2][0])
print('2행1열:',a[2][1])

print('[2차원 튜플의 각 요소 읽기-for문 사용 첫번째]')
#각 행의 열의 수가 다를때
for x in a:
    for y in x:
        print(y,end=' ')
    print()
print('[2차원 튜플의 각 요소 읽기-for문 사용 두번째]')
#각 행의 열의 수가 다를때(언패킹-요소수와 변수의 수가 같아야 한다)
for x,y in a:
    print(x,y)
print('[2차원 튜플의 각 요소 읽기-for문 사용 세번째]')
#각 행의 열의 수가 다를때
for i in range(len(a)):#i는 행 인덱스
    for k in range(len(a[i])):#k는 열 인덱스
        print('{}행 {}열:{}'.format(i,k,a[i][k]),end=' ')
    print()
#문]위 2차원 튜플를 while문으로 출력하여라 .
print('[while문으로 읽기-열의 수가 같을때]')
i=0
while i < len(a):
    x,y = a[i]#언패킹
    print(x,y)
    i+=1
print('[while문으로 읽기-열의 수가 다를때]')
i=0
while i < len(a):
    k=0
    while k < len(a[i]):
        print(a[i][k],end=' ')
        k+=1
    print()
    i+=1