import urllib.request as request
print('[urlopen()함수와 urlretrieve()함수로 HTML소스 읽어오기(스크래핑)]')
#urlopen()함수 : HTTPResponse객체 반환
#               HTTPResponse객체의 read()메소드로 html소스 얻을 수 있다
#urlretrieve()함수: html소스를 파일로 바로 다운받는 함수


#req=request.Request('https://www.naver.com')
#print('value:{},type:{}'.format(req,type(req)))
#print(dir(req))
res=request.urlopen('https://www.naver.com')
print('value:{},type:{}'.format(res,type(res)))
print(dir(res))
print(res)
print(res.status)#상태코드
print(res.headers)
print(type(res.headers))#<class 'http.client.HTTPMessage'>
headers=res.getheaders()
print(headers)#[('응답헤더명','응답헤더값'),(),()....]
print('[응답 헤더 출력]')
for name,value in headers:
    print('헤더명:{},헤더값:{}'.format(name,value))

binarySource =res.read()#응답 데이타 (HTML소스 코드)를 바이너리 형태로 반환
print(type(binarySource))#<class 'bytes'>
htmlSource=binarySource.decode('utf-8')#바이너리 데이타를 디코딩
print(htmlSource)
print(type(htmlSource))#<class 'str'>
#네이버 시작페이지의 전체 html소스를 파일로 저장
with open('naver_urllib1.txt','w',encoding='utf8') as f:
    f.write(htmlSource)
#urlretrieve()함수
retrieve=request.urlretrieve('https://www.naver.com','naver_urllib2.txt')
print('[urlretrieve()함수]')
print(retrieve)
#urlretrieve()를 이용한 다운로드
source,headers=request.urlretrieve('https://www.naver.com','naver_urllib2.txt')
print(source)#html소스가 저장된 파일명
print(headers)#응답헤더











