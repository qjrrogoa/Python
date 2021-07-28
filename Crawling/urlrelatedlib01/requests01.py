#표준 라이브러리가 아님으로 설치 필요
#한글 파라미터가 있는 경우 url인코딩 해야한다 하지만
#requests모듈은 한글 인코딩 불필요.

import requests
print('[모듈명으로 접근 할 수 있는 이름공간]')
print(dir(requests))#모듈명으로 접근 할 수 있는 이름공간
res = requests.get('https://www.naver.com')
print('value:{},type:{}'.format(res,type(res)))#value:<Response [200]>,type:<class 'requests.models.Response'>
print('[변수명(res)으로 접근 할 수 있는 이름공간]')
print(dir(res))
htmlSource=res.text#HTML 소스(일반 텍스트형식의 str):text속성
print('[서버로부터 받은 소스(텍스트 형태)]',htmlSource,sep='\n')
htmlSourceBinary = res.content
print('[서버로부터 받은 소스(바이너리 형태)]',htmlSourceBinary,sep='\n')
print('[서버로부터 받은 소스(바이너리 형태->텍스트형태로 디코딩)]',htmlSourceBinary.decode(encoding='utf8'),sep='\n')
'''
str -> bytes: encode():str의 메소드
bytes -> str: decode():bytes의 메소드
'''
print('[요청 주소]',res.url,sep='\n')
print('[응답 헤더]',res.headers,sep='\n')
for key,value in res.headers.items():
    print('헤더명:{},헤더값:{}'.format(key,value))
print('[상태 코드]',res.status_code,sep='\n')
print('[응답 인코딩]',res.encoding,sep='\n')#네이버의 문서 인코딩 방식
#응답객체로 응답에 대응된 요청 객체
req= res.request
print('value:{},type:{}'.format(req,type(req)))#value:<PreparedRequest [GET]>,type:<class 'requests.models.PreparedRequest'>
print('[요청 방식]',req.method,sep='\n')
print('[요청 주소]',req.url,sep='\n')
print('[요청 헤더]',req.headers,sep='\n')
#응답받은 HTML소스를 파일로 저장하기
with open('naver_requests.html','w',encoding='utf8') as f:
    f.write(htmlSource)





