'''
for 변수  in 반복가능한 객체:

반복가능한 객체(Iteratable):요소가 여러개 있다. 하나씩 꺼내올 수 있다
반복가능한 객체 인지는 dir(객체)를 통해서 알 수 있다
__iter__라는 함수가 있다며 그것은 반복 가능한 객체다

반복기(Iterator): 반복가능한 객체의 __iter__()함수 호출시 반환된 객체.
                              반복기의 __next__()함수를 통해 요소를 하나씩 꺼내온다

                Iterator를 만드는 방법 두가지
                1.class로 만든다(__iter__(self),__next__(self)함수 오버라이딩)
                2.함수로 만들거나(yield키워드로 요소를 반환하는 함수)

'''
print('[문자열에소 헌 문자씩 꺼내오기]')
for element in 'PYTHON':
    print(element)
print('[문자열 길이 만큼 반복하면서 HELLO출력 꺼내온 값은 사용하지 않기]')
for _ in 'PYTHON':
    print('HELLO:',_)
#range()함수(생성자)는 Iterable객체를 반환한다
print('[문자열 길이만큼 반복하기-range()함수 사용]')
for i in range(len('PYTHON')):
    print('i가 %d일때 : %s' % (i,'HELLO'))

print('[range(숫자) 함수 사용하여 (숫자-1)까지 반복]')
for i in range(11):#for(int i=0;i<=10;i++)와 같다
    print(i)
print('[range(시작숫자,끝숫자) 함수 사용하여 (끝숫자-1)까지 반복]')
for i in range(1,11):#for(int i=1;i<=10;i++)와 같다
    print(i)
print('[range(시작숫자,끝숫자,증감폭(양수)) 함수 사용하여 (끝숫자-1)까지 반복]')
for i in range(0,11,2):#for(int i=0;i<=10;i+=2)와 같다
    print(i)
print('[range(시작숫자,끝숫자,증감폭(음수)) 함수 사용하여 (끝숫자+1)까지 반복]')
for i in range(10,-1,-2):#for(int i=10;i<=0;i-=2)와 같다
    print(i)
#반복문을 이용해서 1부터 10까지 누적합:1+2+3+4+5+6+7+8+9+10
#누적합을 저장할 변수 선언]
sum=0
for i in range(11):
    sum+=i
print('{}부터 {}까지 누적합:{}'.format(1,10,sum))
#1부터 10까지 숫자중 2의 배수의 합:2+4+6+8+10
#방법1]2씩 증가하도록 증감식 작성
sum =0
for i in range(0,11,2):
    sum+=i
print('{}부터 {}까지 2의 배수의 누적합:{}'.format(1,10,sum))
#방법2]1부터 1씩증가하면서  10까지 반복
#      i의 값이 2의 배수인 경우에만 누적
sum =0
for i in range(11):
    if i % 2==0:#2의 배수일때만 누적
        sum+=i
print('{}부터 {}까지 2의 배수의 누적합:{}'.format(1,10,sum))
print('for문이 끝난 후 i의 값:',i)
'''
문]1부터 100까지 숫자중 3의 배수 이거나 5의 배수인
숫자의 합을 구해라
단, 3과5의 공배수인 경우 ,누적합에 단 한번만
포함시켜라.
3+5+6+9+10+12+15+18+20+21+24+25+27+30......
'''
sum =0
for i in range(101):
    if i %3 ==0 or i % 5 ==0:
        sum +=i
print('{}부터 {}까지 3과5의 배수의 누적합:{}'.format(1,100,sum))
'''
문]1부터 100까지 숫자중 3의 배수 이거나 5의 배수인
숫자의 합을 구해라
단, 3과5의 공배수는 제외시켜라
즉 15,30,45,60..은 제외
3+5+6+9+10+12+18+20+....
'''
#방법1] or 하고 and연산 사용
sum =0
for i in range(101):
    if (i % 3 == 0 or i % 5 == 0) and i % 15 !=0:
        sum += i
print('{}부터 {}까지 3과5의 배수의 누적합(공배수제외):{}'.format(1,100,sum))
#방법2]^(XOR)연산 사용
sum =0
for i in range(101):
    if (i % 3 == 0) ^ (i % 5 == 0):
        sum += i
print('{}부터 {}까지 3과5의 배수의 누적합(공배수제외):{}'.format(1,100,sum))
'''
이중 for문 :for문 안의 for문
이중 for문에서 바깥 for문은 행(row)를 의미
안쪽 for문은 열(column)을 나타낸다
'''
repeatCount=0
for i in range(3):
    for k in range(3):
        repeatCount+=1
        print('HELLO ',repeatCount)
'''
1 0 0 0 
0 1 0 0 
0 0 1 0
0 0 0 1 처럼 출력해 보자
0 0 0 0
'''
for i in range(5):#행을 의미
    for k in range(4):#열을 의미
        # 행과 열이 같을때 1출력 아니면 0출력
        if i == k:
            print(1,' ',sep='',end='')
        else:
            print(0, ' ', sep='', end='')

    print()#줄바꿈
'''
* 0 0 0 1  (0,3) 
* 0 0 1 0  (1,2)
* 0 1 0 0  (2,1)
* 1 0 0 0  (3,0)처럼 출력해 보자
'''
#방법1]
print('[증가폭 사용]')
for i in range(4):
    for k in range(4):
        # 행과 열의 합이 3일때 1출력 아니면 0출력
        if k+i == 3:
            print(1,end=' ')
        else:
            print(0, end=' ')
    print()  # 줄바꿈
#방법1]
print('[감소폭 사용]')
for i in range(1,5):
     for k in range(4,0,-1):
         if i==k:
            print(1, end=' ')
         else:
            print(0, end=' ')
     print()  # 줄바꿈
'''
*
* *
* * *
* * * *
* * * * *  를 출력하여라 (이중 for문 이용)         
'''
for i in range(5):
    for k in range(5):
        if i >= k:
            print('%-2c' % '*',end ='')
    print()
'''
문]아래 형식대로 구구단을 출력
2 * 1 = 2   3 * 1 = 3   4 * 1 = 4........9 * 1 = 9
2 * 2 = 4   3 * 2 = 6   4 * 2 = 8........9 * 2 =18
..
..
2 * 9 = 18  3 * 9 = 27  4 * 9 =36....... 9 * 9 = 81    
'''
for i in range(1,10):
    for k in range(2,10):
        print('%-2s * %-2s = %-4s' % (k,i,k*i),end='')
    print()
