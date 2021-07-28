#부모클래스
#자식의 생성자 정의시 부모의 생성자를 super()로 명시적으로 호출하지 않으면
#부모 생성자는 호출되지 않는다
#즉 부모의 생성자를 호출하여 부모의 속성을 초기화 하려면 반드시
#super().__init__()를 호출해 해야 한다
class Person:
    def __init__(self,name,age):
        print('부모의 __init__()메소드(생성자)')
        self.name = name
        self.age=age
    def eat(self):
        print(self.name+'님께서 드신다')
    def printPerson(self):
        print('이름:{},나이:{}'.format(self.name,self.age),end='')
#자식 클래스
class Student(Person):
    # 자식의 생성자(__init__())를 정의안해도 아래 코드가 생략된거와 같다
    '''
    def __init__(self,name,age):
        super().__init__(name,age)

    '''

    # 단, 아래처럼 자식에서 __init__를 정의시에는
    # 반드시 super().__init__()를 명시적으로 호출해야 한다
    def __init__(self,name,age,hakbun):
        super().__init__(name,age)
        self.hakbun=hakbun
        print('자식의 __init__()메소드(생성자)')

    def study(self):
        #상속받은 부모의 속성 접근: self사용 혹은 super() (부모와 속성명이 충돌시)
        # self. 으로 접근:자신의 모든 멤버 접근가능(부모에게 상속 받은 거 포함)
        # super(). 으로 접근:부모의 멤버만 뜬다(자식에서 확장한 멤버는 안뜬다)
        print('나이가 {}살인 {}가 공부한다'.format(self.age,self.name))
    def printStudent(self):
        super().printPerson()
        print(',학번:',self.hakbun,sep='')


#student = Student()#TypeError: __init__() missing 2 required positional arguments: 'name' and 'age'
student = Student('가길동',30,2021)
print('이름:',student.name)
student.study()
student.printStudent()