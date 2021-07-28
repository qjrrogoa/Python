'''
1.abc 모듈을 import한다(abc는 abstract base class의 약자)
2.클래스의 (괄호) 안에 metaclass=ABCMeta를 지정
3.메서드 위에 @abstractmethod를 붙여서 추상 메서드로 지정
4.pass로 빈 메소드 정의
'''
from abc import *

class Abstract(metaclass=ABCMeta):
    #생성자는 가질수 있다
    def __init__(self,attr):
        print('추상 클래스의 생성자')
        self.attr=attr
    # 추상 메소드-구현부가 없어야 한다(오버라이딩이 목적)
    @abstractmethod
    def abstractMethod(self):
        pass
    # 일반 메소드도 가질 수 잇다
    def genealMethod(self):
        print('추상 클래스의 일반 메소드')
#추상 클래스 인스턴스화
#abs = Abstract('추상 클래스')#TypeError: Can't instantiate abstract class Abstract with abstract method abstractMethod
class General(Abstract):
    #pass

    def abstractMethod(self):
        print('자식에서 오버라이딩')

#gen = General('자식클래스')#TypeError: Can't instantiate abstract class General with abstract method abstractMethod
gen = General('자식클래스')
gen.genealMethod()
gen.abstractMethod()