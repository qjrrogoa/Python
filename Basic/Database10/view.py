def showMenu():#메뉴 보여주기
    print('=' * 50)
    print('1.입력 2.수정 3.삭제 4.조회 9.종료')
    print('=' * 50)
    return int(input('메뉴 번호를 입력하세요?'))

def dataInput(*args):#사용자로부터 여러 항목을 입력받기 위한 UI

    list_ = list()#빈 리스트 list_ = []
    for arg in args:
        list_.append(input('{}을 입력하세요?'.format(arg)))
    return list_ #입력받은 값을 리스트로 반환

def messageInput(msg):
    return input('{}하려는 제목을 입력하세요?'.format(msg))
def showSearchRecords(records,msg):
    #찾는 레코드가 있으면  숫자반환 없으면 -1 반환
    if len(records) !=0:
        print('*' * 40)
        for no,title,_,postdate,_,name in records:
            print(no,title,str(postdate)[:10],name,sep=' | ')
        print('*' * 40)
        if msg:
            return int(input(msg+'하려고하는 번호를 입력하세요?'))
    else:
        return -1

