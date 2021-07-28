print('[클래스 속성 과 인스턴스 속성')
#클래스 속성 : __init__(self)메소드 안이 아닌 클래스 안에 선언한 변수(self없이)
#          클래스명.속성로 접근
#          모든 인스턴스화된 객체가 공유한다
#인스턴스 속성:self.변수 로 선언한 변수   인스턴스변수.속성로 접근

class Person:
    count =0;#클래스 속성
    def __init__(self,name):
        self.info='사람 클래스입니다'#인스턴스 속성
        self.name=name#인스턴스 속성
        #self.count += 1#도 가능하나 self로 접근하면 count가 인스턴스 속성인지 클래스 속성인지 애매모호
        # 클래스안에서 클래스 속성 접근 : 자신 클래스 안에서도 반드시 클래스명.클래스속성
        Person.count+=1
    def print(self):
        print('지금까지 생성된 총 객체 수:',Person.count)
print('[클래스명으로 클래스 속성 접근]')
print(Person.count)
#인스턴스화
person1 = Person('가길동')
person2 = Person('나길동')
person1.print()
person2.print()
print('[인스턴스 변수로 클래스 속성 접근]')
#파이썬은 속성 이나  메서드를 찾을 때 인스턴스-> 클래스 순으로 찾는다.
#그래서 인스턴스 속성이 없으면 클래스 속성을 찾게 됨으로 문제 없이 동작은 한다.
print(person1.count)#[o]역시 인스턴스 변수로 접근하면 인스트턴스 속성인지 클래스 속성인지 애매모호
print(person2.count)
