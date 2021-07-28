print('[클래스 상속-오버라이딩]')
'''
 -부모 클래스에 있는 메서드를 동일한 이름으로 재정의 하는 것을 
  메서드 오버라이딩(Overriding)이라고 한다. 
 이렇게 메서드를 오버라이딩하면 부모 클래스의 메서드 무시되고 
 오버라이딩한 메서드가 호출된다.
 - 메소드 오버라이딩은 원래 기능을 유지하면서 새로운 기능을 추가할때 주로  사용한다
'''
class Base:
    def __init__(self,attr):
        self.attr=attr
    def getInfo(self):
        return '부모의 속성 attr:{}'.format(self.attr)
    def printInfo(self):
        print(self.getInfo())
class Derived(Base):
    def __init__(self,attr,attr2):
        super().__init__(attr)
        self.attr2 =attr2
    # 오버라이딩
    def getInfo(self):
        return '{},자식의 속성 attr2:{}'.format(super().getInfo(),self.attr2)
    def printInfo(self):
        print(self.getInfo())

dev = Derived('base','derived')
print(dev.getInfo())
dev.printInfo()