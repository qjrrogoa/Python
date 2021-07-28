import pymysql

#메뉴에 따른 입력,수정 및 삭제,조회 하기

def connect():#Connection객체 반환
    return pymysql.connect(
        host='localhost',
        user='kosmo',
        password='1234',
        db='kosmodb',
        charset='UTF8',  # 반드시 UTF8(utf8), UTF-8는 에러
        # ※cursorclass=pymysql.cursors.DictCursor는 딕셔너리 형태로 출력되고
        # 이 부분을 생략하면 결과가 튜플 형태로 출력된다.
        cursorclass=pymysql.cursors.DictCursor
    )
def close(conn,cursor):#커넥션 객체 닫기
    if cursor:
        cursor.close()
    if conn:
        conn.close()
def showMenu():#메뉴 보여주기
    print('=' * 50)
    print('1.입력 2.수정 3.삭제 4.조회 5.메뉴다시보기 9.종료')
    print('=' * 50)

def getMenuNumber():#사용자로부터 메뉴번호 입력 받기
    return int(input('메뉴번호를 입력하세요?'))

def getMember():#사용자 정보 입력받기(입력 혹은 수정시)
    print('입력 혹은 수정 정보를 입력하세요?')
    name=input('이름?')
    age = input('나이?')
    return name, age#튜플 반환 (name,age)와 같다
    #return [name,age]
def getSearchNo(cursor):
    # 수정 혹은 삭제하려는 사람의 이름 입력받기
    name = input('수정 혹은 삭제하려는 사람의 이름을 입력하세요?').strip()
    #쿼리 실행
    cursor.execute('SELECT no FROM member WHERE name =%s',(name,))
    # 페치
    member=cursor.fetchone()
    if member:#찾는 사람이 있으면 키값 반환
        return member['no']
    else:#없으면 member는 None즉 None반환
        return member

def menuExecute(menuNumber,cursor,conn):
    if menuNumber == 1:#입력
        member=getMember()
        cursor.execute('INSERT INTO MEMBER(NAME,AGE,postdate) VALUES(%s,%s,now())',member)
        conn.commit()
        print('입력되었습니다')
    elif menuNumber == 2:#수정
        no=getSearchNo(cursor)
        if no:
            #리스트 반환시
            #member = getMember()
            #member.append(no)
            #cursor.execute('UPDATE member SET name=%s,age=%s WHERE no=%s', member)
            #튜플 반환시
            name,age=getMember()#언패킹
            cursor.execute('UPDATE member SET name=%s,age=%s WHERE no=%s',(name,age,no))
            conn.commit()
            print('수정되었습니다')
        else:
            print('찾는 사람이 없습니다')
    elif menuNumber ==3:#삭제
        no = getSearchNo(cursor)
        if no:
            cursor.execute('DELETE FROM member WHERE no=%s', (no,))
            conn.commit()
            print('삭제되었습니다')
        else:
            print('찾는 사람이 없습니다')
    elif menuNumber == 4:#조회
        cursor.execute('SELECT * FROM MEMBER ORDER BY NO DESC')
        members=cursor.fetchall()
        if len(members) ==0:
            print('=====등록된 회원이 없습니다=====')
        else:
            print('*' * 40)
            #헤더 출력하기
            print('%-4s%-10s%-4s%s' % ('번호','이름','나이','가입일'))
            #데이타 출력
            for member in members:
                print('%-4s%-10s%-4s%s' % (member['NO'],member['NAME'],member['AGE'],str(member['POSTDATE'])[:10]))
            print('*' * 40)
    else:
        showMenu()

if __name__ == '__main__':
    # 데이타베이스 연결하기
    conn = connect()
    # 쿼리실행용 Cursor객체 얻기
    cursor = conn.cursor()
    #메뉴 보여주기
    showMenu()
    while True:
        #사용자로부터 메뉴 입력받기
        menuNumber = getMenuNumber()
        if menuNumber == 9:
            print('프로그램을 종료합니다')
            break;

        menuExecute(menuNumber,cursor,conn)

    #자원닫기
    close(conn,cursor)




