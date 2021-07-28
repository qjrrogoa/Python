from flask_restful import abort

TODOS={
    'todo1':{'task':'REST API만들기'},
    'todo2': {'task': 'Flask 앱 만들기'},
    'todo3': {'task': '그냥 놀기'},
}

def abort_if_todo_doesnt_exist(todo_id):
    if todo_id not in TODOS:
        abort(404, message="Todo {} doesn't exist".format(todo_id))