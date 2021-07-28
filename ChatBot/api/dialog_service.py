from flask_restful import Resource,reqparse
from flask import make_response,jsonify
import dialogflow
from settings.config import DIALOG_CONFIG




class DialogService(Resource):


    def response_from_dailogflow(self,project_id, session_id, message, language_code):
        # step1. DialogFlow와 사용자가 상호작용할 세션 클라이언트 생성
        session_client = dialogflow.SessionsClient()

        # session_path는 projects/프로젝트아이디/agent/sessions/세션아이디로 생성된다.
        session_path = session_client.session_path(project_id, session_id)
        print('[session_path]', session_path, sep='\n')
        if message:  # 사용자가 대화를 입력한 경우. 대화는 utf-8로 인코딩된 자연어. 256를 넘어서는 안된다.
            # step2. 사용자 메시지(일반 텍스트)로 TextInput생성
            '''
                text : '사용자가 입력한 대화'
                language_code : 'ko'
            '''
            text_input = dialogflow.types.TextInput(text=message, language_code=language_code)
            print('text_input', text_input, sep='\n')

            # step 3. 생성된 TextInput객체로 QueryInput객체 생성(DialogFlow로 전송할 질의 생성)
            query_input = dialogflow.types.QueryInput(text=text_input)
            print('query_input', query_input, sep='\n')

            # step 4. DialogFlow로 SessionClient객체. detect_intent()메소드로
            #   QueryInput객체를 보내고 다시 봇 응답(Responses섹션에 등록한 대화)을 받는다
            #   즉 A DetectIntentResponse instanc
            response = session_client.detect_intent(session=session_path, query_input=query_input)
            print('response', response, sep='\n')
            print('type(response)', type(response), sep='\n')

        return response.query_result.fulfillment_text  # 다이얼로그 플로우 봇이 응답한 텍스트

    def post(self): #오버라이딩
        parser = reqparse.RequestParser()
        # 사용자 입력 메시지 : 파라미터명 - message
        parser.add_argument('message')

        # 세션 아이디 : 파라미터명 - session_id
        parser.add_argument('session_id')

        # 파라미터 받기
        args = parser.parse_args()

        # 프로젝트 아이디 가져오기
        project_id = DIALOG_CONFIG['PROJECT_ID']

        # 사용자앱에서 받은 메시지를 다이얼로그 플로우로 보내기(응답을 해준다.)
        fulfillmetnText = self.response_from_dailogflow(project_id, args['session_id'], args['message'], 'ko')

        return jsonify({'message': fulfillmetnText})




