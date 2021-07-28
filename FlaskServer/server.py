from waitress import serve
from app import app
print("서버가 시작되었습니다.")
serve(app,host='0.0.0.0',port=5000)