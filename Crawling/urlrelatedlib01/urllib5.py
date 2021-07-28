#POST방식
#urlopen(요청URL) 혹은  urlopen(Request객체) : GET방식
#req=Reqquest(요청url,data=params)
#urlopen(Request객체): POST방식
import urllib.request as request
import urllib.parse as parse
params = parse.urlencode({'id':'kosmo','pw':'kosmo1234'})
print('byte형으로 인코딩 전:',params)#id=kosmo&pw=kosmo1234
#TypeError: POST data should be bytes, an iterable of bytes, or a file object. It cannot be of type str
#encode():문자열 을 bytes형 으로 변환
#str타입인 params를 <class 'bytes'>타입으로 변환

params = params.encode(encoding='utf-8')#bytes형으로 변환
print('byte형으로 인코딩 후:',params)

headers={'User-agent':'Mozilla/5.0'}
url = 'https://nid.naver.com/nidlogin.login'
req = request.Request(url,headers=headers,data=params)
res = request.urlopen(url)
print('응답코드:',res.status)
print('요청방식:',req.get_method())
print('[응답 데이타]')
print(res.read().decode('utf-8'))

