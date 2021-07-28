import sqlite3

try:
    #데이타베이스 연결
    conn = sqlite3.connect('sampledb.db')
    #쿼리 전송을 위한 커서객체 얻기
    cur=conn.cursor()
    #쿼리 실행
    cur.execute("SELECT * FROM member ORDER BY _ID DESC")
    #데이타 Fetch:쿼리문이 SELECT일때
    # 방법1:fetchall()-리스트 반환  [(),(),()....] ()가 하나의 레코드에 해당
    '''
    rows=cur.fetchall()
    print('value:{},type:{}'.format(rows,type(rows)))
    for _id,name,tel in rows:
        print('번호:{},이름:{},전번:{}'.format(_id,name,tel))
    '''
    # 방법2:fetchone()
    '''
    row = cur.fetchone()#하나의 레코드를 튜플로 반환:(컬럼1,컬럼2,...)
    print('value:{},type:{}'.format(row, type(row)))
    #컬럼수 모를때
    s=''
    for i in range(len(row)):
        s+='{},'.format(row[i])
    print(s[:-1])
    #컬럼수 알때
    print('번호:{},이름:{},전번:{}'.format(row[0],row[1],row[2]))
    '''
    # 방법3:fetchmany(가져올 레코드 수) 갯수 미 지정시 디폴트는 1개
    rows = cur.fetchmany(3)
    for _id, name, tel in rows:
        print('번호:{},이름:{},전번:{}'.format(_id, name, tel))

except Exception as e:
    print(e)
finally:
    #생성한 순서 반대로 닫는다
    cur.close()
    conn.close()