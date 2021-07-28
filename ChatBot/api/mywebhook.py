from flask_restful import Resource,reqparse
from flask import make_response,request,jsonify

class WebHook(Resource):
    def post(self): #post요청 처리 오버라딩
            # 다이얼로그 플로우에서 json으로 응답을 보낸다.
            dialog_response = request.get_json(force=True)
            print('[dialog_response]', dialog_response, sep='\n')

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
            reply = {'fulfillmentText': '{}날짜에 {}를 예약하셨습니다.Right!!!!'.format(date_time, zzikgo_place)}

            return make_response(reply)
