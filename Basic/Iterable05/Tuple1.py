print('[튜플 생성 첫번째 : 빈 튜플]')#클래스나 함수에서 주로 사용
def pprint(obj):
    print('객체:{},타입:{}'.format(obj,type(obj)))
    if not isinstance(obj,float) and not isinstance(obj,int):
        print('객체의 요소 수:',len(obj))
#방법1-()
a=()
pprint(a)
#방법2-tuple():tuple클래스의 생성자
a=tuple()
pprint(a)
print('[튜플 생성 두번째 : 요소가 하나인 튜플]')
b=(1)
pprint(b)
b=1,#혹은 b=(1,)
pprint(b)
print('[튜플 생성 세번째 : 같은 타입의 객체(요소) 저장]')
b=(1,2,3,4,5,)#혹은 b=1,2,3,4,5,
pprint(b)
print('[튜플 생성 세번째 : 다른 타입의 객체(요소) 저장]')
c='가길동',20,3.14,True#괄호 생략
pprint(c)
print('[튜플 언팩킹]')
#튜플의 각 요소를 여러 변수에 나눠 담는 것:언패킹(구조분해)
#단, 변수의 개수가 요소의 개수와 일치해야 한다
c1,c2,c3,c4 = c
pprint(c1)
pprint(c2)#TypeError: object of type 'int' has no len()
pprint(c3)#TypeError: object of type 'float' has no len()
pprint(c4)#TypeError: object of type 'bool' has no len()
print('[튜플 생성 네번째 : 문자열로 튜플 만들기]')
s='PYTHON'
tuple_from_str = tuple(s)
pprint(tuple_from_str)
tuple_from_str = tuple(s.split())#문자열 전체를 하나의 요소로 갖는 리스트 반환->다시 튜플로 변환
pprint(tuple_from_str)
print('[튜플 생성 다섯번째 :tuple(range객체)]')
tuple_from_range=tuple(range(5))
pprint(tuple_from_range)
print('[튜플객체[인덱스] : 해당 인덱스의 값 읽기]')
print('b[0]:{},a[{}]:{}'.format(b[0],len(b)-1,b[len(b)-1]))
print('[튜플의 요소수 구하기:len()]')
print('총 요소수:',len(tuple(range(100,1000,2))))
print('[튜플 슬라이싱]')
#c='가길동', 20, 3.14, True
print(c[1:1])#() 빈 튜플
print(c[1:3])#(20, 3.14)
print(c[1:-3])#1부터 -4(-3-1)까지 ()
#[:끝인덱스] -  처음부터 끝인덱스-1까지
print(c[:4])#('가길동', 20, 3.14, True)
#[시작인덱스:] -  시작인덱스부터 끝까지
print(c[-len(c):])#('가길동', 20, 3.14, True)
#[:] -  모든 요소 슬라이싱
print(c[:])#('가길동', 20, 3.14, True)
print('[for문을 이용해서 튜플의 인덱스 및 요소 가져오기]')
f=('가','나','다','라')
for element in f:#요소만 출력
    print(element)
for index in range(len(f)):##요소와 인덱스 출력
    print('인덱스:{},요소:{}'.format(index,f[index]))
#for 인덱스, 값 in enumerate(순서가 있는 객체):  #인덱스와 값을 동시에 꺼내올 수 있다
for index,element in enumerate(f):#요소와 인덱스 출력
    print('인덱스:{},요소:{}'.format(index,element))




