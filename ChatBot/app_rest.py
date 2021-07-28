#UI는 필요없다 즉 static 및 templates폴더 불필요(UI는 별도 제작)
from flask import Flask
#restfuldyd
from flask_restful import Api
#Rest api요청을 처리할 클래스를 정의한 모듈 import
from api.dialog_service import DialogService
from api.mywebhook import WebHook
import os
from settings.config import DIALOG_CONFIG #프로젝트 아이디/ API키가 설정된 모듈 import

from flask_cors import CORS

app = Flask(__name__)
CORS(app)

app.config['JSON_AS_ASCII']=False

api=Api(app)
os.environ['GOOGLE_APPLICATION_CREDENTIALS']=DIALOG_CONFIG['GOOGLE_APPLICATION_CREDENTIALS']

#요청을 처리할 클래스와 요청 uri매핑
api.add_resource(DialogService,'/message')
api.add_resource(WebHook,'/mywebhook')

if __name__ =='__main__':
    app.run(host='0.0.0.0',port=9292)