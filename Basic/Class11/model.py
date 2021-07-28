import cx_Oracle
from configparser import ConfigParser
from view import View

class Model:
    def __init__(self):#데이타베이스 연결
        config = ConfigParser()#cinfig는 생성자의 지역변수
        config.read('../Database10/oracle.ini',encoding='utf8')# encoding='utf8'는 한글이 포함된 경우
        #2.데이타베이스 연결
        self.conn = cx_Oracle.connect(config['ORACLE']['user'],config['ORACLE']['password'],dsn=config['ORACLE']['url'])
        #3. 쿼리 실행용 커서 생성
        self.cursor = self.conn.cursor()
    def close(self):#커넥션객체 닫기
        if self.cursor:
            self.cursor.close()
        if self.conn:
            self.conn.close()
    def insert(self,list_):#입력처리
        try:
            self.cursor.execute(
                    """
                    INSERT INTO onememo(no,title,content,id) 
                    VALUES(SEQ_ONEMEMO.NEXTVAL,:1,:2,:3)
                    """,list_)
            self.conn.commit()
            return 1
        except Exception as e:
            print(e)
            return 0
    def update(self,list_):#수정처리
        try:
            self.cursor.execute(
                """
                UPDATE  onememo SET title=:1,content=:2 WHERE no=:3
                """, list_)
            self.conn.commit()
            return self.cursor.rowcount
        except Exception as e:
            print(e)
            return -1
    def delete(self,key):#삭제처리
        try:
            self.cursor.execute(
                """
                DELETE FROM  onememo  WHERE no=:NO
                """, {'NO':key})
            self.conn.commit()
            return self.cursor.rowcount
        except Exception as e:
            print(e)
            return -1

    def getSearchRows(self,title):#제목으로 검색해서 검색된 레코드들 반환
        self.cursor.execute(
            '''
            SELECT O.*,M.NAME 
            FROM MEMBER M JOIN ONEMEMO O ON M.ID=O.ID
            WHERE TITLE LIKE '%' || :TITLE || '%'
            ORDER BY NO DESC
            ''',{'TITLE':title}
        )
        #페치
        return self.cursor.fetchall()

    def selectAll(self):#전체 레코드들 반환
        self.cursor.execute(
            '''
            SELECT O.*,M.NAME 
            FROM MEMBER M JOIN ONEMEMO O ON M.ID=O.ID           
            ORDER BY NO DESC
            '''
        )
        #페치
        return self.cursor.fetchall()



if __name__ == '__main__':
    model = Model()
    print(model.conn,model.cursor)
    #print(model.insert(['제목...','내용...','KIM']))
    #print(model.update(['제목수정', '내용수정', '73']))
    #print(model.delete('73'))
    #print(View.showSearchRecords(model.getSearchRows('제목'),'수정'))
    print(model.selectAll())

    model.close()