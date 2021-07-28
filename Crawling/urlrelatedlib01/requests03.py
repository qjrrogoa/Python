#POST방식으로 요청 보내기
#방법1:requests.post(요청url)
#방법2:requests.request('POST',요청url)

#로그인이 필요 없을때는 requests.post()
#로그인이 필요한 경우 세션이 필요하기 때문에
#1.session=requests.Session() 로 세션 객체를 얻고
#2.세션 객체로 session.post()
import requests
#세션이 필요없는 POST 요청
#방법1
#res= requests.post('http://localhost:10004/springapp/Annotation/RequestMappingBoth.do',
#                   data={'UserID':'KIM','UserPWD':'9999'})
#방법2
#res= requests.request('POST','http://localhost:10004/springapp/Annotation/RequestMappingBoth.do',
#                   data={'UserID':'KIM','UserPWD':'9999'})
#세션이 필요한 POST 요청
params = {'id':'KIM','pwd':'9999'}
#세션객체 생성
session = requests.Session()
#세션객체로 post()
params = {'id':'KIM','pw':'9999'}
res= session.post('https://nid.naver.com/nidlogin.login',data=params)
print('[상태코드]',res.status_code)
print('[요청방식]',res.request.method)
print('[응답 데이타]',res.text,sep='\n')

