print('[딕셔너리의 주요 메소드]')
print('1.setdefault(키) 혹은 setdefault(키,기본값)')
a={'name':'가길동','age':20,'addr':'천호동'}
a.setdefault('tall')#a['tall']=None와 같다
print(a)
a.setdefault('weight',30)#a['weight']=30
print(a)
#setdefault는 기존 키값의 value는 수정이 안된다
#a.setdefault('name','가길동2')#수정안됨
#a['name']='가길동2'#수정됨
print('2.update(키=값):기존 키에 해당하는 값이 수정됨')
a.update(name='가길동2')#a['name']='가길동2' 와 같다
print(a)
a.update(tel='010')#없는 키로 update()하면 해당 키가 요소로 추가된다
print(a)
print('3.pop(키) 혹은 pop(키,기본값)')
#삭제한 키의 밸류값 반환
#pop(키) : 키에 해당하는 요소 삭제
#          만약 키가 없다면 에러발생(KeyError)
#pop(키,기본값):키가 없으면 에러 발생하지 않고 그냥 기본값 반환
print(a.pop('weight'))
#del 딕셔너리객체[키]#키가 존재하지 않으면 KeyError발샐 .print문에 사용불가
del a['tall']
print(a)
print('4.popitem() :마지막 요소 삭제.삭제된 요소를 튜플로 반환')
#print('삭제된 요소:',a.popitem())#('tel', '010')
key,value = a.popitem()
print('삭제된 요소 key:{},value:{}'.format(key,value))
print('5. clear(): 전ㅊ페 요소 삭제.반환값 업다')
a.clear()
print(a)#{}
b=dict(institue='KOSMO',loc='가산디지털단지역',course='데이타 분석')
print('6.copy()함수')
c= b.copy()

print('b의 주소:{},c의 주소:{}'.format(id(b),id(c)))
b.update(loc='강남')
print(b)
print(c)
d=b
print('b의 주소:{},d의 주소:{}'.format(id(b),id(d)))
b['loc']='제주도'
print(b)
print(d)
print('7. get(키)함수 get(키,기본값)')
#키가 없어도 에러 발생 안함
#get(없는 키)는 None반환
#get(없는키,기본값)는 기본값 반환
print(b.get('location'))
print(b.get('location','강릉'))
print('8.items()/keys()/values()함수')
x=b.items()
print('value:{},type:{}'.format(x,type(x)))
for key,value in x:
    print('키:{},값:{}'.format(key,value))
y=b.keys()
print('value:{},type:{}'.format(y,type(y)))
for key in y:
    print('키:{}'.format(key))

z=b.values()
print('value:{},type:{}'.format(z,type(z)))
for value in z:
    print('값:{}'.format(value))

#리스트나 튜플의 요소를 키로 사용하여 딕셔너리를 만드는 함수
#dict.fromkeys(리스트나 튜플)는 키에따른 값은 모두 None
#dict.fromkeys(리스트나 튜플,값)는 키에따른 값은 모두 두번째 인자에 지정한 값
print('9. dict.fromkeys(리스트나 튜플)함수 혹은 dict.fromkeys(리스트나 튜플,값)함수')
print(dict.fromkeys([1,2,3,4,5]))
print(dict.fromkeys([1,2,3,4,5],100))


