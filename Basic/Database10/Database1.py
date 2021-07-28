#1. sqlite3 모듈을 import
import sqlite3


try:
    print(sqlite3.version)
    # 2. SQLite DB에 연결. 데이타베이스 파일은 현재 디렉토리에서   오픈 혹은 생성
    conn = sqlite3.connect('sampledb.db')#커넥션 객체 반환
    print('value:{},type:{}'.format(conn,type(conn)))
    # 방법1:
    # 3.커넥션객체의 cursor()메소드로 Cursor 객체생성
    #cur=conn.cursor()
    #print('value:{},type:{}'.format(cur, type(cur)))
    # 4. Cursor 객체의 execute() 명령으로 SQL 쿼리를 실행
    #cur.execute('SELECT * FROM MEMBER')

    # 방법2:
    # 커넥션 객체의 execute(쿼리문)
    cur=conn.execute('SELECT * FROM MEMBER')

    # 5.데이타 Fetch(SQL문이 SELECT일때)
    rows=cur.fetchall()#테이블의 쿼리결과는 [(),(),()] 형태로 반환(리스트)된다.즉 하나의 레코드는 튜플로 만들어진다
    print('value:{},type:{}'.format(rows, type(rows)))
    for no,name,tel in rows:
        print('번호:{},이름:{},전번:{}'.format(no,name,tel))
except Exception as e:
    print(e)
finally:
    # Cusor객체 및 Connection 객체의 close() 메서드로 닫기
    cur.close()
    conn.close()