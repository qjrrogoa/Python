from model import Model
from view import View
class Controller:
    # 생성자 - 모델 생성
    def __init__(self):
        self.model = Model()
    def showSearchRecords(self,msg):
        # 수정/삭제시 검색할 제목 입력받기
        title = View.messageInput(msg)
        # 모델호출- 입력받은 제목으로 검색
        records=self.model.getSearchRows(title)
        #검색된 레코드 디스플레이(사용자가 번호 선택하도록)
        key = View.showSearchRecords(records,msg)
        return key
    #사용자 요청 처리 메소드
    def handleRequest(self,menu):
        if menu == 1:#입력
            #입력 데이타 받기(뷰호출)
            list_ = View.dataInput(*['제목','내용','아이디'])
            #모델 호출
            affected = self.model.insert(list_)
            #뷰호출
            View.showMessage(affected,'입력')
        elif menu == 2:#수정
            key=self.showSearchRecords('수정')
            #수정 데이타 받기(뷰호출)
            list_ = View.dataInput(*['제목', '내용'])
            #위 리스트에 키 추가(키값으로 수정할꺼니까)
            list_.append(key)
            # 모델 호출 - 수정
            affected=self.model.update(list_)
            # 뷰호출
            View.showMessage(affected, '수정')
        elif menu==3:#삭제
            key = self.showSearchRecords('삭제')
            # 모델 호출 - 삭제
            affected = self.model.delete(key)
            # 뷰호출
            View.showMessage(affected, '삭제')
        elif menu==4:#전체 레코드 출력
            #모델 호출
            records=self.model.selectAll()
            #뷰 호출
            View.printRecordsAll(records)
    def close(self):
        self.model.close()