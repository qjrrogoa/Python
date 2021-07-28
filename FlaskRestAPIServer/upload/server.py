import app
from waitress import serve
print('REST API 서버가 시작되었습니다...')
serve(app.app,port=9000,host='0.0.0.0')
