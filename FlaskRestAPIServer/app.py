'''
https://flask-restful.readthedocs.io/en/latest/
1. pip install flask
2. pip install flask-restful
3. pip install flask_cors
'''


from flask import Flask
from flask_restful import Api
from flask_cors import CORS
from api.todo import Todo
from api.todolist import TodoList
from api.upload import Upload

app = Flask(__name__)
#JSON 응답 한글 처리
app.config['JSON_AS_ASCII'] = False

#CORS에러 처리
CORS(app)

# 플라스크 앱(app)을 인자로 하여 Api객체 생성 : 클래스와 URI매핑해서 요청을 라우팅 @app.route('/todos/<todo_id>')와 같은 효과
# 라우팅 즉 @app.route('/todos/<todo_id>')와 같다
api = Api(app=app)

#요청을 처리할 클래스와 요청 uri 매핑(라우팅)
#Api객체.add_resource(클래스명,'/요청url')
#/todos/<todo_id> ul 패턴이면
#get방식이면 todo_id로 조회
#delete방식이면 todo_id로 삭제
#put방식이면 todo_id로 수정

api.add_resource(Todo,'/todos/<todo_id>')

#/todos로 요청시 get방식이면 전체 조회 post방식이면 할 일 등록
api.add_resource(TodoList,'/todos')

#파일 업로드
api.add_resource(Upload,'/upload')

if __name__ == '__main__':
    app.run(port=8000,host='0.0.0.0')
