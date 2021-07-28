#in (not in)  연산자 : 딕션너리에 적용시 딕션너리에 키의 존재여부를 파악할 수 있다
print('[딕셔너리에 in 및 not in연산자 적용하기]')
a=dict(name='홍길동',age=20,addr='가산동')
print('tall' in a)
print('tall' not in a)
print('name' in a)
print('name키 존재' if a.get('name')!=None else 'name키 없음')
print('[for문 사용 첫번째 - for 변수 in 딕셔너리 객체:] ')
for key in a:
    value = a.get(key)
    print('key:{},value:{}'.format(key,value))
print('[for문 사용 두번째 - for 변수 in 딕셔너리 객체.keys():] ')
for key in a.keys():
    value = a.get(key)
    print('key:{},value:{}'.format(key,value))
print('[for문 사용 두번째 - for 변수 in 딕셔너리 객체.items():] ')
for key,value in a.items():
    print('key:{},value:{}'.format(key,value))
'''
for 반복문으로 값을 찾아서 딕셔너리 요소 삭제하면 에러가 발생 
즉 Iterating하는동안 요소를 삭제하면 크기가 변하기때문에..

'''
'''
for key,value in a.items():
    if value=='홍길동':
        del a[key]#RuntimeError: dictionary changed size during iteration
'''''
key_ = None
for key,value in a.items():
    if value=='홍길동':
        key_ = key
#for문이 끝난 후 삭제
del a[key_]
print(a)