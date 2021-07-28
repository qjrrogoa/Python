from flask_restful import Resource,reqparse
from api.todo_data import TODOS,abort_if_todo_doesnt_exist
from flask import make_response,jsonify
import json

#자원을 HTTP method 에 맞게 처리하는 api(메소드)를 정의한 클래스
#1.Resource 상속
class Todo(Resource):
    #2. HTTP 메소드(post,get,put,delete) 별 오버라이딩
    def __init__(self):
        #생성자에서 파라미터 받기
        #step1. RequestParser 객체 생성
        self.parser = reqparse.RequestParser()
        #step2 RequestParser객체에 add_argument('파라미터명')로 모든 파라미터명 추가
        #요청시 파라미터로 전달되는 파라미터명을 인자로 추가
        self.parser.add_argument('task') #파라미터명 task
    #키값에 따른 테이타 조회
    #get(self,매개변수)의 매개변수와 add_resource()의 변수명이 일치해야한다
    #uri 매핑시 api.add_resource(클래스명,'/todos/<todo_id>')
    def get(self,todo_id):
        #요청시 받은 todo_id가 존재하지않는다면 예외발생
        abort_if_todo_doesnt_exist(todo_id)
        # 예 :
        # 뷰 반환 즉 html반환
        # return render_template('index.html',foo=42) 이때는 응답헤더 추가 불가
        # 응답객체 반환. 이때는 응답헤더 추가 가능
        # response=make_response(render_template('index.html',foo=42))
        # response.header['헤더명'] ='헤더값'
        # return response
        # 또한 make_response함수는 JSON으로 응답시 내부적으로 utf8을 사용
        #return TODOS[todo_id]
        #return jsonify(TODOS[todo_id])
        return make_response(TODOS[todo_id]) #make_response(TODOS.get(todo_id)

    #키값(todo_id)에 따른 데이터 삭제 api
    def delete(self,todo_id):
        abort_if_todo_doesnt_exist(todo_id)
        del TODOS[todo_id]
        return jsonify({'success':'삭제 성공했어요'}) # 204는 서버가 요청을 성공적으로 처리했지만 콘텐츠를 제공하지 않는다
                                                             # 튜플 반환('브라우저로 전송할 컨텐츠',상태코드값)
        #return '',204

    def put(self,todo_id):
        abort_if_todo_doesnt_exist(todo_id)
        # 사용자가 전달한 파라미터 받기 : self.parser.parse_args()
        # RequestParser객체의 parse_args메소드로 반환된 값은 todo_id로 요청된 value이다.
        # 즉 파라미터명으로 task 그리고 value로 '수정합니다' 즉 key는 'tsak' value는 전달 '수정합니다' 전달시
        # parse_args()는 {'task':'수정합니다'}로 반환
        args = self.parser.parse_args()
        print('args:',args)
        #'task'라는 키값으로 사용자가 전달한 값으로 수정한 딕셔너리 생성
        task= {'task':args['task']}
        TODOS[todo_id]=task

        return make_response(task,201)