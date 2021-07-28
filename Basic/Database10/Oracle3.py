from model import *
from view import *
import view
#데이타베이스 연결
conn = init()
while True:
    menu=showMenu()
    if menu == 9:
        break
    elif menu == 1:
        list_ = dataInput(*['제목','내용','아이디'])
        print(insert(conn,list_),'행이 입력되었어요')
    elif menu ==2:
        records=getSearchRows(messageInput('수정'),conn=conn)
        key=showSearchRecords(records, '수정')
        list_=dataInput(*['제목','내용'])
        print(update(key,list_,conn),"행이 수정되었어요")
    elif menu==3:
        records = getSearchRows(messageInput('삭제'), conn=conn)
        key = showSearchRecords(records, '삭제')
        print(delete(key,conn), "행이 삭제되었어요")
    elif menu==4:
        records=selectAll(conn)
        showSearchRecords(records,None)

close(conn)