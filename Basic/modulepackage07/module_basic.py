'''
모듈 도큐먼트화 주석
현재 모듈(파일)에 대한 소개글을 적는다
'''
print('[현재 모듈의 이름공간(Namespac)표시]')
x=10#x라는 변수명으로 이름공간에 추가됨
print(dir())#현재 모듈의 이름공간을 리스트로 반환
print('[현재 모듈의 전체 경로 출력]')
print(__file__)#E:\CCH\Workspace\python\modulepackage07\module_basic.py
print('[현재 모듈의 도큐먼트화 주석 출력]')
print(__doc__)
print('[현재 모듈의 모듈명 출력]')
print(__name__)#__main__
print('[특정 모듈(표준 라이브러리에서 제공하는 모듈) 사용하기]')
'''
모듈 읽어오는 순서
1.현재  작업디렉토리
2.환경변수
3.sys.path에 있는 내장 모듈 및 표준 라이브러리 경로
'''
import sys,os
print(dir(os))
print(os.__file__)#C:\Users\kosmo_teacher\AppData\Local\Programs\Python\Python39\lib\os.py
print(os.__doc__)
print(os.__name__)#os
print(dir(sys))#__file__이 없다 즉 sys는  C언어로 만들어져 파이썬에 내장된 모듈로 .py파일(모듈형태)로 제공되지 않는다
#print(sys.__file__)#AttributeError: module 'sys' has no attribute '__file__'
