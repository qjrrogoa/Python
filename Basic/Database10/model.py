from builtins import Exception

import cx_Oracle
from configparser import ConfigParser

def init():#데이타베이스 연결:Connection 객체 반환
    config = ConfigParser()
    config.read('oracle.ini',encoding='utf8')
    return cx_Oracle.connect(config['ORACLE']['user'],config['ORACLE']['password'],config['ORACLE']['url'])

def close(conn):#커넥션객체 닫기
    if conn:
        conn.close()
def insert(conn,list_,*args):#입력처리
    with conn.cursor() as cursor:
        try:
            cursor.execute('INSERT INTO ONEMEMO(NO,TITLE,CONTENT,ID) VALUES(SEQ_ONEMEMO.NEXTVAL,:1,:2,:3)',list_)
            conn.commit()
            return 1
        except Exception as e:
            print(e)
            return 0
def update(key,list_,conn):
    with conn.cursor() as cursor:
        try:
            list_.append(key)
            cursor.execute('UPDATE ONEMEMO SET TITLE=:1,CONTENT=:2 WHERE NO=:3', list_)
            conn.commit()
            return cursor.rowcount
        except Exception as e:
            print(e)
            return 0
def delete(key,conn):
    with conn.cursor() as cursor:
        try:
            print(cursor.execute('DELETE FROM ONEMEMO WHERE NO=:NO', {'NO':key}))
            conn.commit()
            return cursor.rowcount
        except Exception as e:
            print(e)
            return 0
def selectAll(conn):
    with conn.cursor() as cursor:
        try:
            cursor.execute('SELECT O.*,M.NAME FROM MEMBER M JOIN ONEMEMO O ON M.ID=O.ID ORDER BY NO DESC ')
            # 5.패치
            return cursor.fetchall()  # 리스트 반환 ,각 레코드는 튜플
        except Exception as e:
            print(e)
            return None
def getSearchRows(title,conn):
    #수정 혹은 삭제하려는 제목 입력받기
    with conn.cursor() as cursor:
        try:
            cursor.execute('''
            SELECT O.*,M.NAME 
            FROM MEMBER M JOIN ONEMEMO O ON M.ID=O.ID
            WHERE TITLE LIKE '%' || :TITLE || '%'            
            ORDER BY NO DESC ''',{'TITLE':title})
            #패치
            return cursor.fetchall()  # 리스트 반환 ,각 레코드는 튜플
        except Exception as e:
            print(e)
            return None

if __name__ == '__main__':
    conn = init()
    #affected=insert(conn,['제목10','내용10','KIM'])
    #print(affected,'행이 입력되었어요')
    #affected = update(72,['제목텐','내용텐'],conn)
    #print(affected, '행이 수정되었어요')
    #affected = delete(71,conn)
    #print(affected, '행이 삭제되었어요')
    #print(selectAll(conn))
    print(getSearchRows('제목',conn))
    close(conn)


