'''
패키지의 __init__.py에서 from .모듈  import *로 모든 변수, 함수, 클래스를 가져올때
패키지 외부에 공개하고 싶은 변수나 함수 그리고 클래스를
 __all__에 리스트 형태로 지정하면  모듈을 사용하는
 프로그램 시작점에서는 __all__ 변수에
 지정한 것만 사용할 수 있다(즉 지정하지 않은 것은 패키지 외부에 비공개)
 '''
from .module4 import *
__all__ =['getYear','getDate']