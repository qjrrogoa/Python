print('[튜플의 주요 메소드]')
print('1.index(요소):리스트 요소의 인덱스 반환,count(요소):요소의 빈도수 반환')
g='가','나','다','라','나','마','나'
print('"나"의 인덱스:',g.index('나'))
#print('"바"의 인덱스:',g.index('바'))#ValueError: '바' is not in list
if '바' in g:
    print('"바"의 인덱스:', g.index('바'))

print('"나"의 빈도수:',g.count('나'))

print('[튜플의 산술 연산]')#+와 *만 가능
x=1,2,3
y='가','나','다'
print(x+y)
print(y*3)
print(x*0)#튜플에 0이나 음수를 곱하면 빈 튜플 ()가 나온다
#print(x * 3.14)#TypeError: can't multiply sequence by non-int of type 'float'
#in (not in)  연산자 : 리스트에 요소의 존재여부를 파악할 수 있다
z=1,2,3
print(4 not in z)
print(1 in z)












