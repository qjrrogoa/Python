'''
파이썬에는 switch문이 없다
딕션너리 와 사용자 정의 함수를 이용해서 switch문 효과를 낼수 있다
'''
kor=99;eng=60;math=95
avg =(kor+eng+math)//30
#학점을 반환하는 함수:switch
'''
def switch(key):
    #문자열 반환
    return {
        10:'A학점',
        9:'A학점',
        8:'B학점',
        7:'C학점',
        6:'D학점'}.get(key,'F학점')
print('평균:{},학점:{}'.format(avg,switch(avg)))
'''
def switch(key):
    #함수 반환
    return {
        10:lambda : print('A학점'),
        9: lambda: print('A학점'),
        8: lambda: print('B학점'),
        7: lambda: print('C학점'),
        6: lambda: print('D학점'),
        5: lambda: print('F학점'),
        4: lambda: print('F학점'),
        3: lambda: print('F학점'),
        2: lambda: print('F학점'),
        1: lambda: print('F학점'),
        0: lambda: print('A학점'),

    }[key]

#f = switch(avg)
#f()
#value:<function switch.<locals>.<lambda> at 0x000001A9454EF3A0>,type:<class 'function'>
#print('value:%s,type:%s' % (f,type(f)))
switch(avg)()#f = switch(avg);f() 이 두 명령어를  하나의 명령어로


