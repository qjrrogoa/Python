import math
#변수
PI = math.pi
#함수
def add(*args):
    print('{}부터 {second}까지 누적합:{tot}'.format(args[0],second=args[len(args)-1],tot=sum(args)))

#클래스
class MyClass:
    def hello(self):
        print('클래스의 메소드-hello')

print('module02.py모듈의 스페셜변수 __name__ : ',__name__)
if __name__ == '__main__':#현재 파일을 모듈로 사용하지 않고 실행한다면
    print(PI)
    add(*list(range(1,11)))