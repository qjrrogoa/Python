'''
파일 업로드
POSTMAN :
POST : http://localhost:포트번호/upload
Body선택 후 form-data 선택 그리고 key 입력 후 File 선택(text:디폴트)
그리고 다른 값들은 key에 value에 입려4
'''
from flask_restful import Resource,reqparse
from flask import make_response
import werkzeug #
import os
class Upload(Resource):
    def post(self):
        #RequestParser객체 생성 : 요청 파라미터 파싱하는 객체
        parser = reqparse.RequestParser()
        # RequestParser객체에 모든 파라미터 추가
        # 첫번째 인자 'upload'는 파라미터명
        # location='files' 디렉토리 경로가 아니다. 파일 업로드인 경우 반드시 "files"
        parser.add_argument('title') #제목 파라미터명
        parser.add_argument('name') #올린이 파라미터명
        parser.add_argument('upload',location='files',type=werkzeug.datastructures.FileStorage) #<input type="file"
        args = parser.parse_args()
        # args['파라미터명'] 전송한 파라미터 얻기
        # 파일 업로드 처리
        f=args['upload'] #는 FileStorage추가
        filename = f.filename[0:-1] if f.filename[-1] =='"' else f.filename
        f.save('upload{}{}'.format(os.path.sep,filename))
        title = args['title']
        name = args.get('name')
        return make_response({'filename':filename,'title':title,'write':name})
