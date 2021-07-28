'''
try:
    예외가 발생할 만한 코드
except 예외명1:
    예외명1이 발생했을 때 처리할 코드
except 예외명2:
    예외명2가 발생했을 때 처리할 코드

혹은 여러 예외 동시 처리
try:
    예외가 발생할 만한 코드
except (예외명1,예외명2) :
    예외명1 혹은 2가 발생했을 때 처리할 코드
'''
try:
    list_ =list(map(int,input('두 개의 숫자를 입력?(공백)').split()))
    result = list_[0]/list_[1]
    print('{one}/{two}의 결과:{three}'.format(three=result,one=list_[0],two=list_[1]))
    index = int(input('인덱스를 입력하세요?'))
    print('인덱싱:',list_[index])
#3
except Exception as e:
    print('예외 발생:', e)
'''
#2
except (ValueError,ZeroDivisionError,IndexError) as e:#반드시 ()로 감싼다
    print('예외 발생:',e)
'''
'''
#1
#부모 예외가 모든 예외를 모두 잡아 버리기 때문에 아래 except절은 실행이 안된다
#따라서 except Exception:절은 마지막에 위치시키자
#자바처럼 Unreachable Code에러는 발생하지 않는다
except Exception as e:
    print('예외가 발생했어요:',e)
except ValueError:
    print('숫자만 입력하세요')
except ZeroDivisionError:
    print('0으로 나눌수 없어요')
except IndexError as e:
    print('인덱스 범위를 벗어낫어요:',e)
'''