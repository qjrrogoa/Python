print('[클래스의 메소드안에서 메소드 호출하기]')
#모듈 Class2.py의 함수들
def sleep():print('클래스 밖(모듈의) 메소드:sleep()')
def eat():print('클래스 밖(모듈의) 메소드:eat()')

#클래스 정의
class Person:
    def __init__(self,name):
        self.name = name

    def sleep(self): print(self.name + '이(가) 자다')
    def eat(self):print(self.name + '이(가) 먹다')
    def print(self):
        # 클래스안의 인스턴스 메소드 호출시에는 self지정
        self.sleep()
        self.eat()
        # 클래스 밖(모듈)의 함수 호출
        sleep()
        eat()
#인스턴스화
person = Person('가길동')
person.print()


