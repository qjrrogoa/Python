#w+,r+,a+ 모드 : +는 읽기 나 쓰기 기능이 플러스됬다는 의미
print('[w+모드]')#기존 내용 지워지고 새로쓰나 읽기도 가능하다
#w_plus.txt파일 생성후에
#안녕하세요
#HELLO 입력하자
with open('w_plus.txt','w+',encoding='utf8') as f:
    print('읽기가능:{},쓰기가능:{}'.format(f.readable(),f.writable()))
    f.write('123456789')
    #읽기도 가능하니까 위에서 쓴 내용을 읽어보자
    print(f.read())#빈문자열
    #123456789를 출력후 커서가 9다음에 가 있다
    #커서를 파일 맨 앞으로 옮겨야 한다
    f.seek(0)
    print(f.read())
print('[r+모드]')
#r_plus.txt파일 생성후에
#안녕하세요
#HELLO 입력하자
with open('r_plus.txt','r+',encoding='utf8') as f:
    print('읽기가능:{},쓰기가능:{}'.format(f.readable(),f.writable()))
    print(f.read())
    f.write('\n파이썬')
    print('---전체 내용 읽기---')
    f.seek(0)
    print(f.read())
# a_plus.txt파일 생성후에
# 안녕하세요
# HELLO 입력하자
print('[a+모드]')#모드 w와 같으나 기존 내용이 지워지지 않고 추가된다.읽기도 가능(+가 붙어서)
with open('a_plus.txt','a+',encoding='utf8') as f:
    print('읽기가능:{},쓰기가능:{}'.format(f.readable(),f.writable()))
    f.write('\n파이썬')
    print('---전체 내용 읽기---')
    f.seek(0)
    print(f.read())