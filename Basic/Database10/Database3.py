import sqlite3#sqlite3 import
try:
    # 2.데이타베이스 연결
    conn = sqlite3.connect("sampledb.db")
    # 3. 쿼리실행을 위한 Cursor객체 생성
    cur = conn.cursor()
    # 4.쿼리 실행
    records =[('코스모4','1007'),('코스모5','1008'),('코스모6','1009')]
    '''
    for ele in records:
        cur.execute("INSERT INTO member(name,tel) VALUES(?,?)",ele)
    '''
    cur.executemany("INSERT INTO member(name,tel) VALUES(?,?)",records)
    # 5. 커밋
    conn.commit()
    print('여러개의 레코드 입력 성공')
except Exception as e:
    print(e)
finally:
    #6. 자원반납
    cur.close()
    conn.close()