#딕션너리 표현식:기존 딕션너리 객체로 새로운 딕션너리 객체를 생성할때 주로 사용한다
'''
{키:값  for 키[, 값 ] 혹은 [키,]값    in 딕션너리.items() }
{키:값  for 키[, 값] 혹은 [키,]값   in 딕션너리.items() if 조건식}

dict({키:값  for 키[, 값 ] 혹은 [키,]값  in 딕션너리.items()})
dict({키:값  for 키[, 값 ] 혹은 [키,]값  in 딕션너리.items() if 조건식})
딕션너리 표현식으로
특정 값을 기준으로 딕션너리를 다시 생성하는 방식으로 삭제 효과를 구현할 수 있다
'''
keys = ['A','B','C','D']
print('[딕셔너리 표현식 첫번째- {} : 리스트로 생성]')#리스트 요소를 키로 사용
#dict.fromkeys() 사용
a=dict.fromkeys(keys,'PYTHON')
print(a)
#표현식 사용
b = {key:'PYTHON' for key in keys}
print(b)
print('[딕셔너리 표현식 두번째- dict({}) : 리스트로 생성]')

c = dict({key:'PYTHON'+key for key in keys})
print(c)

print('[딕셔너리 표현식 세번째- keys() : 기존 딕셔너리로 생성]')
d={key:len(key) for key in a.keys() }
print(d)

print('[딕셔너리 표현식 세번째- values() : 기존 딕셔너리로 생성]')
e={value:value for value in a.values() }
print(e)

print('[딕셔너리 표현식 네번째- items() : 기존 딕셔너리로 생성]')
f={value:key for key,value in a.items() }#키와 밸류 바꾸기
print(f)

f={'name':'가길동','tel':'010','addr':'가산동'}
#키가 'name'인 요소는 제외-삭제효과
g = {value :key for key,value in f.items() if key != 'name'}
print(g)
