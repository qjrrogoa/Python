#configparser모듈을 사용한 중요 정보 관리
#섹션명은 대소문자 구분.키/값은 구분하지 않는다
#user = maven 혹은 user=maven 는 같다 즉 자동으로 앞뒤 공백 제거
#https://docs.python.org/ko/3/library/configparser.html
import configparser
config = configparser.ConfigParser()#ConfigParser객체 생성
#ini파일 읽기
list_=config.read('oracle.ini')
print(list_)#['oracle.ini']
list_=config.sections()
print(list_)#['section', 'ORACLE', 'DATABASE']
items=config.items()
print(items,list(items),type(items),sep=' | ')
print(list(items))#[('DEFAULT', <Section: DEFAULT>), ('section', <Section: section>), ('ORACLE', <Section: ORACLE>), ('DATABASE', <Section: DATABASE>)]
print(type(list(items)[0][1]))#<class 'configparser.SectionProxy'>
print('[for문 사용]')
for section,proxy in items:
    #print(dir(proxy))#딕셔너리와 유사
    if section == 'ORACLE':
        user=proxy.get('user')
        password = proxy.get('PASSWORD')
        url = proxy['URL']
        print('user:{},password:{},url:{}'.format(user,password,url))
print('[직접 키로 접근]')
#ConfigParser객체['섹션명']['키값']
user = config['ORACLE']['user']
password = config['ORACLE']['password']
url = config['ORACLE']['url']
print('user:{},password:{},url:{}'.format(user,password,url))


#1.모듈 import
import cx_Oracle
#2.데이타베이스 연결
#conn = cx_Oracle.connect(user,password,url)
conn = cx_Oracle.connect(user=user,password=password,dsn=url)
print(conn)
#3.쿼리 실행을 위한 커서객체 얻기
cursor = conn.cursor()
#4.쿼리 실행
#방법1:numbered placeholder -1부터 시작(데이타는 tuple 혹은 list로)
#cursor.execute('INSERT INTO ONEMEMO(NO,TITLE,CONTENT,ID) VALUES(SEQ_ONEMEMO.NEXTVAL,:1,:2,:3)',('제목입니다715','내용입니다715','KIM'))
#방법2:named placeholder -(데이타는 딕셔너리로:키값은 컬럼명으로)
#cursor.execute('INSERT INTO ONEMEMO(NO,TITLE,CONTENT,ID) VALUES(SEQ_ONEMEMO.NEXTVAL,:TITLE,:CONTENT,:ID)',{'TITLE':'제목입니다715_1','CONTENT':'내용입니다715_1','ID':'KIM'})
#cursor.execute('INSERT INTO ONEMEMO(NO,TITLE,CONTENT,ID) VALUES(SEQ_ONEMEMO.NEXTVAL,:TITLE,:CONTENT,:ID)',TITLE='제목입니다715_2',CONTENT='내용입니다715_2',ID='KIM')
#하나의 쿼리문을 여러번 실행:executemany()
#records=[('제목1','내용1','KIM'),('제목2','내용2','KIM'),('제목3','내용3','KIM')]
#cursor.executemany('INSERT INTO ONEMEMO(NO,TITLE,CONTENT,ID) VALUES(SEQ_ONEMEMO.NEXTVAL,:1,:2,:3)',records)
records=[{'TITLE':'제목4','CONTENT':'내용4','ID':'KIM'},{'TITLE':'제목5','CONTENT':'내용5','ID':'KIM'},{'TITLE':'제목6','CONTENT':'내용6','ID':'KIM'}]
cursor.executemany('INSERT INTO ONEMEMO(NO,TITLE,CONTENT,ID) VALUES(SEQ_ONEMEMO.NEXTVAL,:TITLE,:CONTENT,:ID)',records)

#5.commit
conn.commit()
#6.자원 반납
cursor.close()
conn.close()


