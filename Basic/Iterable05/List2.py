print('[리스트의 주요 메소드]')
print('1.append():요소 추가')
a=[1,(2),3]
a.append(4)
a.append(1)#중복 저장가능
a.append(['가','나'])
print(a)#[1, 2, 3, 4, 1, ['가', '나']]
#print(a[len(a)])#IndexError: list index out of range
print(a[len(a):])#[] 6번 인덱스는 없다 하지만 슬라이싱 표현으로 마지막방 다음 요소에 할당 연산자(=)로 추가할 수 있다
#append()함수가 아닌 리스트객체[새로운인덱스]=값로 새로운 요소추가시에는 값은 반드시 반복가능한 객체여야한다
a[len(a):] = [10,20]#구조분해가 되서 각 요소가 하나씩 각 방에 저장됨#a[len(a):] = 10 TypeError: can only assign an iterable
print(a)
print('2.extend():리스트 확장')
b=[1,2,3]
#b.extend(4)#TypeError: 'int' object is not iterable 즉 인자로 반복가능한 객체여야 한다
b.extend([4])#b.extend((4,))
b.extend([5,6])
print(b)#[1, 2, 3, 4, 5, 6]
print('3.insert(인덱스,객체):기존 인덱스 위치에 요소 삽입')
c=[1,2,3]
c.insert(0,'가길동')
c.insert(100,'나길동')#인덱스 범위를 벗어난 경우 항상 len(리스트객체)인덱스에 삽입된다
#c.append('나길동')와 같다
print(c)
print('4.copy():리스트 복사')#원본 리스트가 복사되어 새로운 리스트가 생성되고 그 새로운 리스트의
                           #주소가 저장된다
d=c.copy()
print(d)
print('c의 주소:{},d의 주소:{}'.format(id(c),id(d)))
d[0]=10
print(c)
print(d)
print('5.remove(삭제할 요소):리스트의 요소삭제')#반환값 없다(None)
e=[1,2,3,4,5,2]
e.remove(4)
print(e)#[1, 2, 3, 5, 2]
#동일한 객체를 삭제하는 경우 인덱스가 작은 요소가 삭제됨
print(e.remove(2))#None
print(e)
print('6.pop([인덱스]):리스트의 마지막 요소 삭제')
#pop()는 리스트의 마지막 요소삭제.반환값은 삭제한 요소
#pop(인덱스) : 인덱스에 헤당하는 요소 삭제.
f=[1,2,3,4,5,2]
print(f.pop())
print(f.pop(2))
print(f)
#f.pop(100)#IndexError: pop index out of range
print('7.del 연산자로 리스트 요소 삭제하기')
#변수삭제시 : del 변수명
#del f
#print(f)#NameError: name 'f' is not defined
#del f[:]#f.clear()와 같다
#del f[1:3]
del f[1]#f.pop(1)과 같다
print(f)#[]
print('8.index(요소):리스트 요소의 인덱스 반환,count(요소):요소의 빈도수 반환')
g=['가','나','다','라','나','마','나']
print('"나"의 인덱스:',g.index('나'))
#print('"바"의 인덱스:',g.index('바'))#ValueError: '바' is not in list
if '바' in g:
    print('"바"의 인덱스:', g.index('바'))

print('"나"의 빈도수:',g.count('나'))
print('9.reverse():리스트의 요소를 반대로 정렬')
print(g.reverse())#None #IN-PLACE방식 :새로운 객체가 반환되는 게 아니라 자신이 바뀌는 방식
print(g)
print('10. sort():리스트의 요소 정렬')
g.sort()#디폴트는 오름 차순
print(g)
g.sort(reverse=True)
print(g)#내림차순
print('[리스트의 산술 연산]')#+와 *만 가능
x=[1,2,3]
y=['가','나','다']
#x.extend(y)
#print(x)
print(x+y)#위 두 줄과 같다
print(y*3)
print(x*0)#[]리스트에 0이나 음수를 곱하면 빈 리스트[]가 나온다
#print(x * 3.14)#TypeError: can't multiply sequence by non-int of type 'float'
#in (not in)  연산자 : 리스트에 요소의 존재여부를 파악할 수 있다
z=[1,2,3,]
print(4 not in z)
print(1 in z)










