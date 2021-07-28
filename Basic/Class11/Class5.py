print('[인스턴스 메소드/정적 메소드/클래스 메소드]')
'''
인스턴스 메소드:self(인스턴스화된 객체자신)를 인자로 받는 메소드로 인스턴스 변수로 접근
정적 메소드:self,cls(인스턴스화가 되지 않는 클래스 자신)를 인자로 받지 않는 메소드로 @staticmethod라는 데코레이터를 붙인 메소드
클래스 메소드:cls를 받은 메소드로 @classmethod라는 데코레이터가 붙은 메소드

정적메소드와 클래스메소드는 클래스명.메소드명으로 접근.인스턴스화 불필요
'''
class StringClass:
    clsAttr='클래스 속성'
    # 생성자
    def __init__(self,instanceAttr):
        print('생성자의 self:{},type:{}'.format(self,type(self)))
        self.instanceAttr=instanceAttr
    #인스턴스 메소드
    def slicing(self,start,end):
        print('인스턴스 메소드의 self:{},type:{}'.format(self,type(self)))
        print('인스턴스 메소드에서 클래스 속성에 접근:',StringClass.clsAttr)
        return self.instanceAttr[start:end]
    # 정적 메소드 :인스턴스 속성이 필요 없는 경우 즉 인스턴스 내용과는 상관없이 결과만
    # 구하면 될 때는 정적(혹은 클래스) 메서드를 사용
    '''
                 @staticmethod를 데코레이터라 함
                 @staticmethod
                 def 메소드명([매개변수들]):
                    명령문
    '''
    @staticmethod
    def listToString(delim,lst):
        #print(self)#정적 메소드에서 인스턴스멤버에 접근 불가
        print('정적 메소드에서 클래스 속성 접근:',StringClass.clsAttr)
        return delim.join(lst)

    '''
         정적메소드와 유사하다 그리고 클래스 메서드는 메서드 안에서 클래스 속성 이나
         클래스 메서드에 접근 할 때 주로 사용한다.
         cls는 클래스를 의미한다
        '''
    '''
    @classmethod
    def 메서드(cls[,매개변수들]):
            명령문
    '''
    @classmethod
    def stringToList(cls,delim,value):
        #print(self)#클래스 메소드에서 인스턴스멤버에 접근 불가
        print('클래스 메소드의 cls:{},type:{}'.format(cls,type(cls)))
        print('StringClass:{},type:{}'.format(StringClass,type(StringClass)))
        # 방법1 : 클래스명.클래스속성
        print('클래스 메소드에서 클래스 속성 접근1:',StringClass.clsAttr)
        # 방법2 : cls.클래스속성
        print('클래스 메소드에서 클래스 속성 접근2:', cls.clsAttr)
        print('클래스 메소드에서 정적 메소드 접근:',cls.listToString(delim,list(map(str,[1,2,3,4,5]))))
        return value.split(delim)
print('[정적 메소드 호출:인스턴스화 전]')
value=StringClass.listToString('▲',['한라산','지리산','설악산'])
print(value)
print('[클래스 메소드 호출:인스턴스화 전]')
print(StringClass.stringToList('▲',value))
#인스턴스화
str_= StringClass('PYTHON')
print(str_.slicing(1,4))


