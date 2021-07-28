#import 패키지명
#으로만 가져올수 있도록 __init__.py 초기화 하기
#방법1]아래는  모듈을 필요로하는 페이지에서 import 패키지명
#from . import module3
#방법2]현재 패키지의  module3 모듈에서 모든 것 가져오기
from .module3 import *
'''위는 현재 패키지의(.) 즉 mathemathics디렉토리의  module3를 불러온다
.(점)는 프로그램 시작점으로 사용하는 모듈에서는 에러 발생'''