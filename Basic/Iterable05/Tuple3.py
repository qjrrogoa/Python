#리스트는  a=[표현식] 혹은 a=list(표현식)
#튜플은   a=tuple(표현식)형식으로 하자
#a=(표현식)은 튜플이 아니고 <generator object <genexpr> at 0x00D15DB0>즉 제너레이터객체 반환
print('[튜플 표현식(축약,내포) 미 사용]')
a=(i for i in range(5))
print('객체:{},타입:{}'.format(a,type(a)))
print(dir(a))
#튜플로 변환
print('객체:{},타입:{}'.format(tuple(a),type(tuple(a))))

print('[튜플 표현식(축약,내포) 사용 첫번째 :tuple()생성자]')
a=tuple(i for i in range(5))
print('객체:{},타입:{}'.format(a,type(a)))
print('[튜플 표현식(축약,내포) 사용 두번째]')
a=tuple(i+2 for i in range(5))
print(a)
a=tuple(i > 1 for i in range(5))
print(a)#(False, False, True, True, True)
print('[튜플 표현식(축약,내포) 사용 세번째]')
#항상 식은 조건이 ㅇ참일때문 실행된다
'''    
    for i in range(10):
        if i % 2==0:
            print(i)
'''
a=tuple(i for i in range(10) if i %2 ==0)
print(a)
#이중 for문과 같다
'''
    for i in range(2,10):
        for k in range(1,10)
            print(i*k)

'''
a=tuple(i * k for i in range(2,10) for k in range(1,10))
print(a)
'''
for i in range(2,10): 
    if i==9:
        for k in range(1,10):
            if k==9:
                print(i*k)
'''

a=tuple(i*k for i in range(2,10) if i==9 for k in range(1,10) if k==9)
print(a)
#리스트를 튜플로 변환:tuple(리스트)
#튜플을 리스트로 변환:list(튜플)


