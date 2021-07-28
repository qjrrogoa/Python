#use_module3.py:패키지 mathmathics를 import해서 사용하기
#현재 파일의 위치:modulepackage07에 위치시키자
#mathmathics패키지의 __init__.py를 빈 파일 그대로 유지한 경우(초기화 하지 않음)
'''
print('[import 패키지명.모듈명]')
import mathmathics.module3 #모듈을 import
print(dir())#현재 파일의 이름공간 출력.'mathmatics'만 보임.즉 패키지명.모듈명.으로 접근해야 한다
print(mathmathics.module3.add(10,20))
print(mathmathics.module3.minus(10,20))
'''
print('[import 패키지명]')
import mathmathics #패키지를 import
print(dir())
#import mathmathics 한 경우 mathmathics를 패키지가 아닌 모듈로 인식이되어
#modulepackage07패키지안에서 mathmathics.py를 찾게된다
#print(mathmathics.module3.add(10,20))#AttributeError: module 'mathmathics' has no attribute 'module3'

#해결책은 패키지 초기화 파일(__init__.py)설정을 통해 mathmatics를 패키지로 처리할수 있도록 할 수 있다
#즉 mathmathics패키지의 __init__.py에서 from . import module03 로
#파일을 초기화 하면 정상적으로 실행된다
print(mathmathics.module3.add(10,20))