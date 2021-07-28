#파이썬에서 게터/세터 만들기
'''
#방법1
class Account:
    def __init__(self):
        self.__accNo = None
        self.__name = None
        self.__balance = None
    # 게터
    def getAccNo(self):
        return self.__accNo
    def getName(self):
        return self.__name
    def getBalance(self):
        return self.__balance
    # 세터
    def setAccNo(self,accNo):
        self.__accNo=accNo
    def setName(self,name):
        self.__name=name
    def setBalance(self,balance):
        self.__balance=balance

    def printAccount(self):
        print('예금주:{},계좌번호:{},잔액:{}'.format(self.__name,self.__balance,self.__balance))

#인스턴스화
acc = Account()
acc.printAccount()
#세터로 설정
acc.setAccNo('123-456')
acc.setName('가길동')
acc.setBalance(100)
acc.printAccount()
print('예금주:',acc.getName())
'''
#방법2
#데코레이터 사용하기
##@property사용시 형태는 메소드 형식이나
#속성으로 사용한다 함수객체가 아니다
class Account:
    def __init__(self):
        self.__accNo = None
        self.__name = None
        self.__balance = None
    # 게터
    @property
    def accNo(self):
        return self.__accNo
    # ->다음이 반환타입:함수 바디
    @property
    def name(self)->object:return self.__name
    @property
    def balance(self)->object:return self.__balance

    # 세터
    # 세터 : @메소드명.setter
    @accNo.setter
    def accNo(self, accNo):self.__accNo = accNo
    @name.setter
    def name(self, name):self.__name = name
    @balance.setter
    def balance(self, balance):self.__balance = balance

    def printAccount(self):print('예금주:{},계좌번호:{},잔액:{}'.format(self.__name, self.__balance, self.__balance))

acc = Account()
#게터/세터를 사용할때는 속성처럼 사용(메소드 호출식하면 에러)
#acc.name('나길동')#TypeError: 'NoneType' object is not callable
#세터 호출
acc.name='나길동'
acc.accNo='123-456'
acc.balance=10000
#게터 호출
#print(acc.name())#AttributeError: can't set attribute
print(acc.name)
acc.printAccount()

