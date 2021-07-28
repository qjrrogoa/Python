#1.모듈 import
import cx_Oracle
from configparser import ConfigParser
config = ConfigParser()
config.read('oracle.ini',encoding='utf8')#encoding='utf8'는 한글이 포함된 경우
#2.데이타베이스 연결
conn = cx_Oracle.connect(user=config['ORACLE']['user'],password=config['ORACLE']['password'],dsn=config['ORACLE']['url'])
#3.쿼리 실행을 위한 커서객체 얻기
cursor = conn.cursor()
#4.쿼리 실행
cursor.execute('SELECT O.*,M.NAME FROM MEMBER M JOIN ONEMEMO O ON M.ID=O.ID ORDER BY NO DESC ')
#5.패치
rows = cursor.fetchall()#리스트 반환 ,각 레코드는 튜플
print(rows)
for no,title,_,postdate,_,name in rows:
    print(no,title,str(postdate)[0:10],name,sep=' | ')
cursor.close()
conn.close()



