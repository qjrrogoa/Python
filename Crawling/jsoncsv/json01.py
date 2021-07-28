print('[파이썬 객체를 JSON형태의 문자열로 변경하기]')
import json#파이썬 2.6부터 표준라이브러리로 제공됨

#테스트용 딕셔너리 데이타
member = {'id':'kim','pwd':'1234','name':'가길동','age':20}
#JSON 인코딩:파이썬 객체(딕셔너리)를 JSON문자열로 변경
objToJsonString=json.dumps(member,indent=4,ensure_ascii=False)#indent키워드 인수 지정시 인덴트 적용된 JSON문자열 반환
                                                              #ensure_ascii=False 한글을 유니코드값으로 변경 안하기 위함
print(type(objToJsonString))
print(objToJsonString)
print('[JSON형태의 문자열로 파이썬 객체로 변경하기]')
jsonStringToObj=json.loads(objToJsonString)
print(type(jsonStringToObj))
print(jsonStringToObj)
print(jsonStringToObj['name'])
for key,value in jsonStringToObj.items():
    print(key,value,sep=' : ')


