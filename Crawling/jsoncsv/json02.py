#https://jsonplaceholder.typicode.com/users
print('[1.requests 모듈 사용]')
import requests #Response객체의 json()함수:JSON형태의 문자열을 파이썬 객체로 변경
res = requests.get('https://jsonplaceholder.typicode.com/users')
print(type(res.text),res.text,sep='\n')
users=res.json()#res.text는 str이지만 res.json()는 파이썬객체(리스트 혹은 딕션너리)
print(type(users),users,sep='\n')
print('[데이타 추출하기]')
for user in users:
    print('==={}의 정보==='.format(user['name']))
    for key,value in user.items():
        #print(key,value,sep=' | ')
        if isinstance(value,dict):
            print('--------%s--------' % key)
            for ky,val in value.items():
                print('{} : {}'.format(ky,val))
        else:
            print('{} : {}'.format(key, value))
print('[2.urlib.request 모듈 및 json모듈 사용]')
import urllib.request as request
import json

res = request.urlopen('https://jsonplaceholder.typicode.com/users')
users = res.read().decode('utf-8')
print(type(users))#<class 'str'>
print(users)
users= json.loads(users)#JSON형태의 문자열을 파이썬 객체(리스트나 딕셔너리)로 변환
print('[데이타 추출하기]')
for user in users:
    print('==={}의 정보==='.format(user['name']))
    for key,value in user.items():
        #print(key,value,sep=' | ')
        if isinstance(value,dict):
            print('--------%s--------' % key)
            for ky,val in value.items():
                print('{} : {}'.format(ky,val))
        else:
            print('{} : {}'.format(key, value))


