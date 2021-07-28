import sqlite3#1. sqlite3 모듈을 import
try:
    # 2. SQLite DB에 연결. 데이타베이스 파일은 현재 디렉토리에서   오픈 혹은 생성
    conn=sqlite3.connect('sampledb.db')
    # 3.커넥션객체의 cursor()메소드로 Cursor 객체생성
    cur=conn.cursor()
    # 4.Cursor객체의 execute()메소드로 쿼리 실행
    # 방법1:Parameter Placeholder방식
    # 튜플로 데이타 설정
    #cur.execute('INSERT INTO member(name,tel) values(?,?)',('라길동','010-1234'))
    # 리스트로 데이타 설정
    #cur.execute('INSERT INTO member(name,tel) values(?,?)',['마길동','011-1234'])
    # 방법2:Named Placeholder
    # ?대신 :컬럼명으로
    cur.execute('INSERT INTO member(name,tel) values(:name,:tel)', ['바길동', '019-1234'])
    # 5. commit:실제 테이블에 반영(쿼리문이 Insert/Delete/Update일때)
    conn.commit()
    print('입력 성공했어요')
except Exception as e:
    conn.rollback()
    print(e)
finally:
    # 6.Cusor객체 및 Connection 객체의 close() 메서드로 닫기
    # 커서객체부터 닫는다
    cur.close()
    conn.close()
