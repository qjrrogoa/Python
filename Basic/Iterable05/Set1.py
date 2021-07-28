#순서가 없기때문에 출력시 순서없이 출력된다.
#단,숫자로만 이루어진 세트는 오름차순으로 출력된다
#단 자리수가 다른 경우
print('[집합 생성 첫번째:빈 집합]')
a={}
print(type(a))
a=set()
print(type(a))
print('[집합 생성 두번째:{}]')#순서 없이 출력된다
a={4,10,282,5,20}
b={'4','10','282',5,'19'}
print(a)
print(b)
print('[집합 생성 세번째:set()-리스트나 튜플 요소를 집합으로 변환시]')
#a=set(1,2,3,4,5)#TypeError: set expected at most 1 argument, got 5
#a=set([1,2,3,4,5])#혹은 a=set((1,2,3,4,5)) =>{1,2,3,4,5}
a=set([i for i in range(1,6)])#리스트나 튜플을 집합으로 변환
a=set(range(1,6))#range객체를 집합으로 변환
print(a)
print('[집합 생성 네번째:set(문자열)]')
a={'HELLO'}
print('value:{},type:{}'.format(a,type(a)))
a=set('HELLO')
print('value:{},type:{}'.format(a,type(a)))
print('[집합 생성 다섯번째:집합안에 집합]')
#a={(1,2),[3,4]}#TypeError: unhashable type: 'list'
a={(1,2),(3,4)}#[o]반드시  모든 요소가 튜플이어야 한다
#a={{'name':'가길동','age':20}}#TypeError: unhashable type: 'dict'
#a={{1,2},{3,4}}#TypeError: unhashable type: 'set'
print(a)