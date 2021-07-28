import numpy as np
import timeit #timeit는 작은 파이썬 코드들의 실행시간을 측정할 수 있는 모듈
#timeit.timeit(stmt='pass', setup='pass', timer=<default timer>, number=100000, globlas=None)
'''
stmt : 실행할 code(statement)를 String타입으로 전달.
setup : 해당 code(statement)를 실행하기 전에 선행되어야 할 code를 string 타입으로 전달
number : code(statement)를 몇번 수행할 것인지 횟수를 지정.
timer는 따로 설정하지 않고 default timer로 수행해도 무방
위 parameter들 중에 setup부분에서 importfmf gownjdiwlaks
사용자가 생성한 method나 사용자 정의 type(module 사용 포함) 이 가능
'''

#파이썬 리스트와 NumPy배열 성능비교
#파이썬 리스트는 반복하면서 리스트의 요소를 하나씩 꺼내어 계산을 하지만
#NumPy 배열은 반복없이 배열의 각 요소와 스칼라(2)를 동시에 연산하기 때문에 훨씬 빠르다.
#0부터 99까지 제곱하기를 100000번 반복 : 파이썬 리스트


'''
start_time = timeit.default_timer()
li = list(range(100))
for _ in range(1000000):
    for i in li:
        i**2
end_time = timeit.default_timer()
print(end_time - start_time)
'''
#24초
#위의 코드를 한 줄로
#print(timeit.timeit(stmt='[i**2 for i in li ]',setup='li = list(range(100))',number=1000000))


#0부터 99까지 제곱하기를 1000000번 반복 : numpy배열

'''
start_time = timeit.default_timer()
nparrr = np.arange(100)
for _ in range(1000000):
        nparr**2
end_time = timeit.default_timer()
print(end_time - start_time)
'''
#0.6초
#print(timeit.timeit(stmt='nparr**2',setup='import numpy as np;nparrr = np.arange(100)',number=1000000))

