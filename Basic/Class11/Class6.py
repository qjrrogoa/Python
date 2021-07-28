print('[비공개 속성 및 비공개 메소드 만들기]')
'''
-클래스밖에서 접근 불가한 멤버
-클래스안에서만 접근 가능
-클래스 밖에서 마음대로 값을 변경하면 안되는 속성등에 적용한다
-비공개 속성은 메소드를 통해 값을 변경하도록 한다
self.__속성명=값  - 비공개 속성
def __메소드명(self[매개변수]): - 비공개 메소드
    pass

__속성=값  - 비공개 클래스 속성
'''
class PrivateClass:
    __clsAttr='비 공개 클래스 속성'
    def __init__(self,value):
        self.publicAttr=value#공개 속성
        self.__privateAttr= None#비공개 속성
    # 비 공개 메소드
    def __privateMethod(self):
        print('비 공개 인스턴스 메소드')
    # 공개 메소드
    def publicMethod(self,value):
        # 비공개 속성 값 설정
        self.__privateAttr = value
        print('비 공개 인스턴스 속성:',self.__privateAttr)
        print('비 공개 클래스 속성:', PrivateClass.__clsAttr)
        # 비 공개 메소드 호출
        self.__privateMethod()

#print(PrivateClass.__clsAttr)#AttributeError: type object 'PrivateClass' has no attribute '__clsAttr'

print('[클래스명의 이름공간 출력]')
print(dir(PrivateClass))
print(PrivateClass._PrivateClass__clsAttr)#[O]__classAttr속성명이  _PrivateClass__classAttr로 맹글링됨 즉 대부분의 OOP언어처럼 완전한 private은 아니다
#인스턴스화
pc = PrivateClass(1000)
print('[인스턴스변수의 이름공간 출력]')
print(dir(pc))
#print(pc.__privateAttr)#AttributeError: 'PrivateClass' object has no attribute '__privateAttr'
print(pc._PrivateClass__privateAttr)#[o]None
pc.publicMethod(10000)
print(pc._PrivateClass__privateAttr)#10000
