from flask import Flask,render_template,request,jsonify,session
import os
import dialogflow

import uuid #세션 아이디로 사용
from settings.config import DIALOG_CONFIG #프로젝트 아이디/ API키가 설정된 모듈 import

app = Flask(__name__)

app.config['JSON_AS_ASCII']=False

#session을 위한 시크릿 키 설정 : 임의의 문자열 - 세션에 값 설정시 반드시 필요
app.secret_key='dfadsfadmcxv'

# API키를 환경변수로 등록
os.environ['GOOGLE_APPLICATION_CREDENTIALS']=DIALOG_CONFIG['GOOGLE_APPLICATION_CREDENTIALS']


@app.route('/')
def index():
    # 랜덤하게 유니크한 식별자 생성(세션아이디로 사용)
    # 사용자별 유니크한 값 생성하게 세션(세션은 딕셔너리의 형태로 저장)에 저장
    # 세션의 유효기간 기본값이 31일
    session['session_id']=str(uuid.uuid4())
    return render_template('index.html')





@app.route('/message',methods=['POST'])
def handleMessage():
    #사용자 UI(Client App)에서 보낸 대화를 받는 함수
    #받은 대화는 다시 DialogFlow로 보낸다
    message = request.form['message']
    print('사용자 UI에서 받은 메시지',message)

    #프로젝트 아이디 가져오기
    project_id = DIALOG_CONFIG['PROJECT_ID']

    #사용자앱에서 받은 메시지를 다이얼로그 플로우로 보내기(응답을 해준다.)
    fulfillmetnText = response_from_dailogflow(project_id,session['session_id'],message,'ko')

    return jsonify({'message':fulfillmetnText})

def response_from_dailogflow(project_id, session_id, message, language_code):
    #step1. DialogFlow와 사용자가 상호작용할 세션 클라이언트 생성
    session_client = dialogflow.SessionsClient()

    #session_path는 projects/프로젝트아이디/agent/sessions/세션아이디로 생성된다.
    session_path = session_client.session_path(project_id,session_id)
    print('[session_path]',session_path,sep='\n')
    if message: #사용자가 대화를 입력한 경우. 대화는 utf-8로 인코딩된 자연어. 256를 넘어서는 안된다.
        #step2. 사용자 메시지(일반 텍스트)로 TextInput생성
        '''
            text : '사용자가 입력한 대화'
            language_code : 'ko'
        '''
        text_input=dialogflow.types.TextInput(text=message,language_code=language_code)
        print('text_input',text_input,sep='\n')


        # step 3. 생성된 TextInput객체로 QueryInput객체 생성(DialogFlow로 전송할 질의 생성)
        query_input = dialogflow.types.QueryInput(text=text_input)
        print('query_input',query_input,sep='\n')

        # step 4. DialogFlow로 SessionClient객체. detect_intent()메소드로
        #   QueryInput객체를 보내고 다시 봇 응답(Responses섹션에 등록한 대화)을 받는다
        #   즉 A DetectIntentResponse instanc
        response=session_client.detect_intent(session=session_path,query_input=query_input)
        print('response',response,sep='\n')
        print('type(response)',type(response),sep='\n')

    return response.query_result.fulfillment_text #다이얼로그 플로우 봇이 응답한 텍스트

    # projects/프로젝트아이디/agent/sessions/세션아이디로 생성된다

#웹 후크 서비스 : 즉 다이얼로그 플로우가 인텐트 매칭 후
# 아래 API서비스(웹 후크)를 POST로 요청한다
# 전제조건
#1. 웹 후쿠를 적용할 인텐트 선택후 fulfillment메뉴에서 enable설정
#2. 해당 봇의 좌측 메뉴인 fullfillments탭에서 아래 url을 등록(localhost및 http는 불가)

@app.route('/mywebhook',methods=['POST'])
def mywebhook(): #fulfillment를 enable로 설정한 인텐트로 진입했을 때 DialogFlow가 이 URL요청
    #다이얼로그 플로우에서 json으로 응답을 보낸다.
    dialog_response=request.get_json(force=True)
    print('[dialog_response]',dialog_response,sep='\n')

    # 아래는 챗복 UI에 사용자가 입력한 Full text
    # query = dialog_response['queryResult']['parameters'] #사용자 입력분 예]예약해주세요
    # 아래는 엔터티 즉 파라미터명으로 값 추출(단 해당 엔터티에 parameters가 등록된 경우)
    # 대표 엔터티명으로 비교하면 된다(그럼 모든 동의어도 처리가 된다)
    # 아래에서 'zzikgo_place'은 개발자 정의 엔터티



    zzikgo_place = dialog_response['queryResult']['parameters']['zzikgo_place'][0]
    print('[zzikgo_place]', zzikgo_place, type(zzikgo_place), sep='\n')
    if '제주도' in zzikgo_place:
        # 웹브라우를 띄우자
        import webbrowser
        webbrowser.open_new('https://m.visitjeju.net/kr#null')

    date_time = dialog_response['queryResult']['parameters']['date-time'][0]
    reply = {'fulfillmentText':'{}날짜에 {}를 예약하셨습니다.Right!!!!'.format(date_time,zzikgo_place)}


    return jsonify(reply)


if __name__ == '__main__':
    app.run(host='0.0.0.0',port='8282')
