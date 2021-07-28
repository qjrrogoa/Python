import urllib.request as request
import urllib.parse as parse
#url에 한글이 포함되면 에러:
#url="https://www.google.com/search?q=%ED%8C%8C%EC%9D%B4%EC%B0%B8"
#url="https://www.google.com/search?q=파이참"
#request.urlopen(url)
url="https://www.google.com/search?q="
encoding=parse.quote('파이참')
print(encoding)#%ED%8C%8C%EC%9D%B4%EC%B0%B8
encoding=parse.quote_plus('파이참')#이 함수를 권장함
print(encoding)#%ED%8C%8C%EC%9D%B4%EC%B0%B8

#res=request.urlopen(url+encoding)#urllib.error.HTTPError: HTTP Error 403: Forbidden
#프로그램으로 접근하는것이 아니라 브라우저로 접근하는 거로 인식하도록 요청헤더 추가
#urlopen(Request객체) 혹은 urlopen(url주소) 로 오픈
req = request.Request(url+encoding,headers={'user-agent':'Mozilla/5.0'})
res = request.urlopen(req)
data=res.read().decode('utf-8')
with open('google.html','w',encoding='utf8') as f:
    f.write(data)
print('[quote()함수와 quote_plus()함수 인코딩 비교]')
#URL 인코딩 함수:quote() 및 quote_plus()함수 비교
encQuote = parse.quote('한글 : 영어')#빈공백 %20
encQuotePlus = parse.quote_plus('한글 : 영어')#빈공백 +
print('quote():{},quote_plus():{}'.format(encQuote,encQuotePlus))
print('[urlsplit(str)함수]')
#urlsplit(주소):URL을 각 부분으로 나눠 튜플로 반환
urls = parse.urlsplit(url)
print(urls)#SplitResult(scheme='https', netloc='www.google.com', path='/search', query='q=', fragment='')
print(dir(urls))
for url in urls:
    print(url)
print(tuple(urls))
print('protocol:{},domain:{},path:{},query:{}'.format(urls.scheme,urls.netloc,urls.path,urls.query))
# urlunsplit():나눈 URL을 합치는 함수
print('[urlulsplit(SplitResult타입)함수]')
print(type(parse.urlunsplit(urls)))#<class 'str'>
print(parse.urlunsplit(urls))
#urlencode(딕셔너리):딕셔너리를 쿼리스트링 형태로 인코딩하는 함수
#                   {키1:값1,키2:값2}를 키1=값1&키2=값2
print('[urlencode(딕셔너리)함수]')
dic ={'q':'파이참 ','oq':'파이참 '}
print(parse.urlencode(dic))



