#클래스의 속성(인스턴스 속성)만들기
#인스턴스화 된 모든 객체가 갖는 속성이 됨.즉 모든 인스턴스에 존재하는 속성이 된다
print('[클래스의 인스턴스 속성 만들기 1 : __init__메소드안에서 self.속성명 = 값 혹은 인스턴스 메소드 안에서]')
class Person:
    def __init__(self,name,age):
        self.name=name
        self.age = age
        self.desc =None
    def print(self):#인스턴스 메소드
        # 클래스안에서 인스턴스 속성에 접근시 : self.속성명
        print('이름:{},나이:{}'.format(self.name,self.age))
        # 이 메서드(print)를 호출해야만 속성(self.method)이 생성된다.
        # 호출전까지는 없는 속성이다
        self.method='이 메소드는 정보를 출력하는 메소드'

#인스턴스트 화(객체화)
person1 = Person('가길동',20)
#클래스 밖에서 속성 접근 : 인스턴스변수.속성명
print('name:{},age:{},desc:{}'.format(person1.name,person1.age,person1.desc))
#person1.print()호출 전
print('person1.print()호출전 이름공간:',dir(person1))
#print('method속성:',person1.method)#AttributeError: 'Person' object has no attribute 'method'
person1.print()
#person1.print()호출 후
print('person1.print()호출후 이름공간:',dir(person1))
print('method속성:',person1.method)

person2 = Person('나길동',30)
person2.print()
print('name:{},age:{},desc:{},method:{}'.format(person2.name,person2.age,person2.desc,person2.method))
print('[클래스의 인스턴스 속성 만들기 2 : 인스턴스화 후 인스턴스변수.속성명 = 값 속성 추가]')#해당 인스턴스에만 존재하는 속성이다
person2.addr='나산동'
print(person2.addr)#[o]
#print(person1.addr)#AttributeError: 'Person' object has no attribute 'addr'

