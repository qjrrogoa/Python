from flask_restful import Resource,reqparse
from api.todo_data import TODOS,abort_if_todo_doesnt_exist
from flask import make_response,jsonify

#1. Resource 상속 받는다
class TodoList(Resource):
    def __init__(self):
        #생성자에서 파라미터 받기
        #step1. RequestParser 객체 생성
        self.parser = reqparse.RequestParser()
        #step2 RequestParser객체에 add_argument('파라미터명')로 모든 파라미터명 추가
        #요청시 파라미터로 전달되는 파라미터명을 인자로 추가
        self.parser.add_argument('task') #파라미터명 task

    def get(self):
        #딕셔너리를 반환하면 json으로 반환된다
        #한글처리를 하기위해 make_response()함수 사용
        #내부적으로 utf로 인코딩하여 응답을 만든다

        #return TODOS #한글이 유니코드로 전송
        #return jsonify(TODOS) #한글 정상
        return make_response(TODOS)

    def post(self):
        # 사용자가 전달한 파라미터 받기 : self.parser.parse_args()
        # step1. add-argument('파라미터명')로 RequestParser객체에 파라미터명 추가(생성자에서 이미 함)
        # 2. 추가된 모든 파라미터의 인수를 구문 분석(파싱)하고
        # 결과를 네임스페이스로 리턴하는 parse_args() 함수 호출
        self.parser.add_argument('title')
        #모든 파라미터 받기
        args = self.parser.parse_args() #{'task':'사용자 입력 값','title':'사용자 입력 값'}
        print(args,type(args),sep=' | ')
        next_id=max(map(int,map(lambda s : s[4:],TODOS.keys())))+1
        todo_id = 'todo'+str(next_id)
        # task의 값은 파라미터로 받은 값으로 설정
        TODOS[todo_id]={'task':args['task']}
        return make_response(TODOS[todo_id])
