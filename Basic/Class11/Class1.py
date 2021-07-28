'''
접근 제한자가 없다 .
따라서 캡술화도 없다
생성자 오버로딩도 없다
즉 클래스에선 무조건 __init__()이 하나만 와야 하고,
마치 private처럼 비공개 속성을 위해선 변수 혹은 함수 앞에
언더바 __를 붙여야한다
'''
#클래스 정의:__init__ 스페셜 메소드(생성자에 해당) 미 정의한 경우
#__init__(self):
#    pass
#가 생략된거와 같다
#class 클래스명:혹은  class 클래스명(object):
#클래스명은 대문자로 시작하자
class Person:#class Person(object):와 같다
    '''
    클래스 독스트링
    사람 클래스입니다
    클래스 바로 밑에 위치 시킨다
    '''
    def sleep(self):#인스턴스 메소드
        '''
        메소드 독스트링
        sleep()메소드 입니다다
       :return:반환값 없다
        '''
        print('자다')
    def eat(self):
        print('먹다')
#인스턴스화  :클래스명()
person1 = Person()
print('value:{},type:{},주소:{}'.format(person1,type(person1),id(person1)))
person1.sleep();person1.eat()
person2 = Person()
print('value:{},type:{},주소:{}'.format(person2,type(person2),id(person2)))
print('[클래스 doc string  및 메소드 독 스트링]')
print(Person.__doc__)#클래스명.__doc__ 혹은 인스턴스변수.__doc__ : 클래스 독 스트링
print(person1.__doc__)
print(Person.sleep.__doc__)#클래스명.메소드명.__doc__ 혹은 인스턴스변수.메소드명.__doc__ : 메소드 독 스트링
print(person1.sleep.__doc__)
print(person1.eat.__doc__)#None
#클래스 정의: __init__ 스페셜 메소드(생성자에 해당) 정의
class Person2(object):
    def __init__(self,name):
        self.name = name
        print('생성자')
    def sleep(self):print(self.name+'이(가) 자다')
    def eat(self):
        print(self.name+'이(가) 먹다')
# 인스턴스화
person3 = Person2('가길동')
print('value:{},type:{},주소:{}'.format(person3,type(person3),id(person3)))
print(person3.name)#인스턴스 속성에 접근
person3.sleep();person3.eat()
#인스턴스변수가 특정 클래스의 인스턴스인지 확인
#isinstance(인스턴스변수,클래스명)
print(isinstance(person1,Person))
print(isinstance(person1,Person2))
