#use_module2.py:모듈 module2.py를 import해서 사용하기
'''
import module2
print('[import 모듈명]')
print(dir())#dir()함수로 현재 파일의 namespace출력:
            #이름공간에 module02만 있으므로 module02.으로 접근
print(dir(module2))#module2의 namespace출력

#module2모듈에 있는 변수/함수/클래스 사용하기
#모듈명.변수 혹은 모듈명.함수명() 모듈명.클래스명()
print('변수:',module2.PI)
print('함수:',end='')
module2.add(*list(range(1,6)))
print('클래스:',end='')
mc=module2.MyClass()
mc.hello()
'''
'''
print('[import 모듈명 as 별칭]')
import module2 as md2
print(dir())#module2가 아닌 md2가 이름공간에 있기 때문에 md2로 접근
print('변수:',md2.PI)
print('함수:',end='')
md2.add(*list(range(1,6)))
print('클래스:',end='')
mc=md2.MyClass()
mc.hello()
'''
print('[from 모듈명 import * 혹은 변수,함수,클래스]')
#from module2 import *
#print(dir())#현재 파일의 이름공간
#print('변수:',PI)#모듈명을 붙이지 않고 바로 접근
from module2 import add,MyClass
print(dir())
#print('변수:',PI)#NameError: name 'PI' is not defined
print('함수:',end='')
add(*list(range(1,6)))
print('클래스:',end='')
mc=MyClass()
mc.hello()




