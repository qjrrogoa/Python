import pymysql
from MySQL3 import connect,close

try:
    conn=connect()
    cursor=conn.cursor()
    cursor.execute("select * from member order by no desc")
    # 데이타 Fetch
    # 방법1:fetchall()
    '''
    rows = cursor.fetchall()
    for row in rows:
        print('{} | {} | {} | {}'.format(row['NO'],row['NAME'],row['AGE'],str(row['POSTDATE'])[:10]))
    '''
    '''
    # 방법2:fetchone()
    row = cursor.fetchone()
    print('{} | {} | {} | {}'.format(row['NO'], row['NAME'], row['AGE'], str(row['POSTDATE'])[:10]))
    '''
    # 방법3:fetchmany(숫자)
    rows = cursor.fetchmany(3)
    for row in rows:
        print('{} | {} | {} | {}'.format(row['NO'], row['NAME'], row['AGE'], str(row['POSTDATE'])[:10]))
except Exception as e:
    print(e)
finally:
    close(conn,cursor)
