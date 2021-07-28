'''
예외 발생시키기
raise Exception([에러메시지])
'''
'''
print('[함수 밖에서 raise키워드 사용 - try: except:절 미 사용]')
value = int(input('숫자 입력?'))
if value % 2 !=0:
    raise Exception('%d는 짝수가 아니예요' %  value)#콘솔창에 빨간줄로 모든 에러 내용 표시
    print('raise 명령어 이후 출력문')#에러 안남(Unreachable code:자바)

print('{}는 짝수'.format(value))
'''
'''
print('[함수 밖에서 raise키워드 사용 - try: except:절 사용]')
try:
    value = int(input('숫자 입력?'))
    if value % 2 !=0:
        raise Exception('%d는 짝수가 아니예요' %  value)#콘솔창에 빨간줄로 모든 에러 내용 표시
        print('raise 명령어 이후 출력문')

    print('{}는 짝수'.format(value))
except Exception as e:
    print(e)
'''
print('[함수 안에서 raise키워드 사용]')#try: except:처리 불필요
#함수 호출한쪽으로 예외를 던지기때문에 호출한 곳에서 try: except:처리하자
def isEven():
    value = int(input('숫자 입력?'))
    if value % 2 != 0:
        raise Exception('%d는 짝수가 아니예요' % value)  #함수를 빠져 나간다
    print('{}는 짝수'.format(value))

try:
    isEven()
except Exception as e:
    print(e)

