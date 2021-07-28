import pymysql
try:
    conn = pymysql.connect(
        host='localhost',
        user='kosmo',
        password='1234',
        db='kosmodb',
        charset='UTF8'
    )
    cur = conn.cursor()
    #※Parameter Placeholder방식:%s사용 (sqlite3는 ?,pymysql는 %s)
    #executemany()로 여러 레코드 입력
    '''
    members =[]
    persons = int(input('인원수를 입력하세요?'))
    for _ in range(persons):
        name = input('이름 입력?')
        age = input('나이 입력?')
        member = (name,age)
        members.append(member)
    cur.executemany("INSERT INTO MEMBER(NAME,AGE) VALUES(%s,%s)",members)
    conn.commit()
    '''
    #execute()로 여러 레코드 입력
    persons = int(input('인원수를 입력하세요?'))
    for _ in range(persons):
        name = input('이름 입력?')
        age = input('나이 입력?')
        member = (name, age)
        cur.execute("INSERT INTO MEMBER(NAME,AGE) VALUES(%s,%s)",member)
    conn.commit()

except Exception as e:
    print(e)
finally:
    cur.close()
    conn.close()