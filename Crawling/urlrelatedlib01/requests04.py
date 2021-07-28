import requests

#REST API서버(스프링으로 구축)에서 보내는 json형태의 문자열을
#바로 json()함수를 사용해서 딕션너리 객체로 만들기
#import json #json을 import할 필요없다 requests 패키지에 포함이 되어있다

res = requests.get('https://jsonplaceholder.typicode.com/photos')
#https://jsonlint.com/에서 res.text로 출력한거를 유효성검사
#json()함수를 사용하면
#json.decoder.JSONDecodeError: Expecting property name enclosed in double quotes
#에러발생 즉 서버측에서 json데이타를 만들때는 "(double  quotation)으로 감

#Response객체의 json()함수: json형태의 문자열(res.text)을 파이썬의 딕션너리로 바꿔주는 함수

items = res.json()#json형태의 문자열을 딕셔너리로 변경
for dic in items:
    for key,value in dic.items():
        print(key,value,sep=' : ')



print(type(items))#<class 'list'>
#파이썬의 리스트를[{},{},{},...]->"[{},{},{},...]" 즉 문자열로 변경
items='['+','.join(list(map(str,items)))+']'


with open('jsonplace1.json','w',encoding='utf-8') as f:
    f.write(items.replace("'",'"'))


with open('jsonplace2.json','w',encoding='utf-8') as f:
    f.write(res.text)
#print(res.json())

