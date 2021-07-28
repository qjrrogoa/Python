#use_module4.py:from절을 사용해서  module4 사용하기
'''
print('[from 패키지.모듈명 import * 혹은 변수,함수,클래스]')
#from date.module4 import  *
from date.module4 import  getYear,getMonth
print(dir())
print('년도:',getYear())
print('월:',getMonth())
print('일:',getDate())
'''
print('[from 패키지 import * 혹은 변수,함수,클래스]')
from date import *
print(dir())
#print('년도:',getYear())#[x]초기화 파일 __init__.py설정 전.NameError: name 'getYear' is not defined
print('년도:',getYear())#[O]초기화 파일 __init__.py설정 후
print('년도:',getDate())
#print('년도:',getMonth())#NameError: name 'getMonth' is not defined