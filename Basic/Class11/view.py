class View:
    @staticmethod
    def showMenu():#메뉴 UI 보여주기
        print('=' * 50)
        print('        1.입력 2.수정 3.삭제 4.조회 9.종료')
        print('=' * 50)
        return int(input('메뉴 번호를 입력하세요?'))
    @staticmethod
    def dataInput(*args):#사용자 입력용 UI
        list_ = []
        for arg in args:
            list_.append(input('{}를(을) 입력하세요?'.format(arg)))
        return list_
    @staticmethod
    def messageInput(msg):
        return input('{}하려는 제목을 입력하세요?'.format(msg))
    @staticmethod
    def showSearchRecords(records,msg): # 찾는 레코드가 있으면  숫자반환 없으면 -1 반환
        if len(records) !=0:
            print('*' * 40)
            for no,title,_,postdate,_,name in records:
                print(no,title,str(postdate)[0:10],name,sep=" | ")
            print('*' * 40)
            return int(input(msg+'하려고하는 번호를 입력하세요?'))
        else:
            return -1
    @staticmethod
    def showMessage(affected,msg):
        print('{}행이 {}되었습니다'.format(affected,msg))

    @staticmethod
    def printRecordsAll(records):  # 전체 레코드 출력
        print('=' * 50)
        for no, title, _, postdate, _, name in records:
            print(no, title, str(postdate)[0:10], name, sep=" | ")
        print('=' * 50)


if __name__ == '__main__':
    View.showMenu()
    #print(View.dataInput(*['제목','내용','아이디']))
    #print(View.messageInput('수정'))
    import datetime
    records=[
        (1,'제목1','내용1',datetime.datetime(2021,7,19,9,50,50),None,'가길동'),
        (2, '제목2', '내용2', datetime.datetime(2021, 7, 19, 9, 50, 50), None, '나길동')

    ]
    print(View.showSearchRecords(records,'삭제'))

