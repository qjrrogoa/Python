#use_module1.py:모듈 module1.py를 import해서 사용하기
import module1
print('[모듈 불러오기 : import 모듈명(.py를 제외한 파일명)]')
import module1#여러 번 import해도 최초 import시에만 실행됨 즉 한번만 import하면 된다
print('[모듈 module1의 이름공간 출력]')
print(dir(module1))
print('[모듈 module1의 PI변수 사용하기:모듈명.변수]')
print(module1.PI)