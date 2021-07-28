#※urllib3는 requests모듈 설치시 함께 설치된다.
#고로 파일명을 urllib3.py로 하지 말아라

import urllib.request as request
print('[urlopen()함수와 urlretrieve()함수로 이미지 읽어오기(스크래핑)]')

'''

res = request.urlopen('https://mblogthumb-phinf.pstatic.net/MjAxODA3MDFfMjk4/MDAxNTMwNDM2Njg0MDU4.YeAGbE7jt59wT86AHumNLxwR0D2UNqkIMkq7f77__dgg.viSMkcW_c0Ky9zdUQD3chGf8tMR5O7LEgIncXehS-ewg.PNG.sarang2594/Python_%EC%9E%85%EB%AC%B8_%EB%AF%B8%EB%8B%88%EC%BD%98%EB%8B%A4.png?type=w800')
print(res.status)
print(res.read())#이미지 파일임으로 decode() 불필요
data = res.read()
with open('anaconda.png','wb') as f: #파일 저장은 되나 OKB
    f.write(data)
'''


#마치 브라우저가 요청하도록 요청헤더 설정
req = request.Request('https://mblogthumb-phinf.pstatic.net/MjAxODA3MDFfMjk4/MDAxNTMwNDM2Njg0MDU4.YeAGbE7jt59wT86AHumNLxwR0D2UNqkIMkq7f77__dgg.viSMkcW_c0Ky9zdUQD3chGf8tMR5O7LEgIncXehS-ewg.PNG.sarang2594/Python_%EC%9E%85%EB%AC%B8_%EB%AF%B8%EB%8B%88%EC%BD%98%EB%8B%A4.png?type=w800',headers={'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'})
print(dir(req))
print('요청방식:{},요청서버:{}'.format(req.get_method(),req.host))
print(req.get_header('User-agent'))
print(req.headers)
res = request.urlopen(req)
data = res.read()
with open('anaconda.png','wb') as f: #파일 저장 정상
    f.write(data)


request.urlretrieve('https://mblogthumb-phinf.pstatic.net/MjAxODA3MDFfMjk4/MDAxNTMwNDM2Njg0MDU4.YeAGbE7jt59wT86AHumNLxwR0D2UNqkIMkq7f77__dgg.viSMkcW_c0Ky9zdUQD3chGf8tMR5O7LEgIncXehS-ewg.PNG.sarang2594/Python_%EC%9E%85%EB%AC%B8_%EB%AF%B8%EB%8B%88%EC%BD%98%EB%8B%A4.png?type=w800','anaconda2.png')

