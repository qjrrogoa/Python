#함수안에서 yeild키워드를 사용하면 그 함수는 제너레이터를 반환
#제너레이터는 이터레이터를 생성하는 객체다
#이터레이터는 next를 호출할때마다 값을 생성하는 객체다
print('[return 키워들 사용해 값을 반환하는 일반적인 함수]')
def general_function():
    print('첫번째 출력문')
    return 0
    print('두번째 출력문')
    return 1
    print('세번째 출력문')
    return 2
print(general_function,type(general_function))
print('[general_function의 이름공간]')
print(dir(general_function))#__iter__없다
print('[general_function함수 3번 호출]')
print(general_function())
print(general_function())
print(general_function())
print('[yield 키워드를 사용해 값을 반환하는 함수(제너레이터:generator)]')
def generator_function():
    print('첫번째 출력문')
    yield 0
    print('두번째 출력문')
    yield 1
    print('세번째 출력문')
    yield 2

print(generator_function,type(generator_function))
print('[generator_function의 이름공간]')
print(dir(generator_function))#__iter__없다
generator_=generator_function()#generator반환
print('[generator의 이름공간]')
print(dir(generator_))#__iter__ 있다
it=generator_.__iter__()#<class 'generator'>반환 즉 generator는 iterator다
print('[generater_function함수 3번 호출한거와 같다]')
print(it.__next__())#__next__()함수 호출
print(it.__next__())
print(it.__next__())
#print(it.__next__())#더이상 yield할 값이 없으면 StopIteration발생
print('[yield키워드를 사용하는 이유]')
def myrange_return(max_):
    index,list_ = 0,[]
    while index < max_:
        list_.append(index)
        index+=1
    return list_#10만개의 메모리가 필요
print(myrange_return(100000))
print(sum(myrange_return(100000)))

def myrange_yield(max_):#리스트 불필요.필요할때마다 숫자 생성
                        #즉 모든 요소를 메모리에 올려두지않고 next를 호출시 필요한 요소들을 생성
                        #메모리 사용측면에서 유리
    index = 0
    while index < max_:
        yield index
        index+=1
print(myrange_yield(100000))#generator객체
print(sum(myrange_yield(100000)))




