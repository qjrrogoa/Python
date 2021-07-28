num1 =100
print('[if문 형식 첫번째로 짝/홀수 판단]')
#조건식이 두번 실행됨.
if num1 % 2==0:
    print('짝수')
if num1 % 2!=0:
    print('홀수')
print('[if문 형식 두번째로 짝/홀수 판단]')
#조건식 한번만 실행됨.
if num1 % 2==0:
    print('짝수')
else:
    print('홀수')
#[조건부 표현식- 다른 언어에서는 삼항연산자라 함]
'''
 if ~else문과 같다.
 코드를 짧게 표현할때 주로 사용(if ~else문  대신에)
 구문]
 변수 = 값 if 조건문 else 값
'''
print('[조건부 표현식(삼항연산자)로 짝/홀수 판단]')
result = '짝수' if num1 % 2==0 else '홀수'
print(result)
#※else는 항상 if문과 짝을 이루어야 한다. 단독 사용불가
if num1 %2 == 0:
    print("짝수")
print("num1는 ",num1)#if문 과 무관
#[x]아래 else는 짝을 이루는 if문이 없다.
'''
else :
    print("홀수")
'''
#문]한 문자를 입력받아 숫자인지 아닌지
#   if ~else문 과  조건부 표현식를 이용하여 판단하여라.
char = input('한 문자를 입력?')
print('[if ~else문]')
if '0' <= char <='9':
    print('숫자')
else:
    print('숫자가 아님')
print('[조건부 표현식]')
print('숫자' if '0' <= char <='9' else '숫자가 아님')