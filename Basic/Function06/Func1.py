#함수 정의 하기전에 함수 호출하기
#파이썬은 코드를 순차적으로 실행하기 때문에 함수 정의전에 호출하면
#helloPython()#NameError: name 'helloPython' is not defined
#함수 정의하기
def helloPython():
    print('Hello Python')
#함수 호출하기
helloPython()
print(helloPython())#반환값이 없을때는 None
#빈 함수 정의하기
def empty():
    pass

print(empty())#None

#함수 독스트링 사용하기
def printMessage(msg):
    '''
                함수 독스트링:주석처럼 사용할 수 있으나 하나의 명령문이다
                문자열을 입력받아 출력하는 함수
                :param msg:입력받은 문자열
                :return:반환값은 없다
            '''
    msg ='입력값:{}'.format(msg)
    '''
    아래 print(msg)는 입력값을 출력하기위한 출력문이다(주석처럼 사용하는 스트링)
    '''
    print(msg)


printMessage('Hello Python')
print('[함수 독스트링 출력하기]')
print(printMessage.__doc__)
#함수 결과값 반환하기
def add(a,b):
    result =a+b
    return result#함수는 return문을 만나면 모든 실행을 종료하고 빠져 나간다
                 #즉 아래 코드는 실행되지 않는다
    print('return문 이후 출력문')
result = add(10,20)
print(result)
print(add(10,20))
#return 키워드 응용하기
def entrance(age):
    if not (20<=age<=40):
        print('입장불가')
        return
    print('즐거운 시간 보내세요')

entrance(10)
entrance(30)
entrance(40)

def add(x,y):
    c=x+y
    return c,x,y#(c,x,y)와 같다 튜플 반환

r = add(10,20)
print('value:{},type:{}'.format(r,type(r)))
z,x,y = add(100,200)#구조분해(언패킹)
print('{} + {} = {}'.format(x,y,z))
