'''
try:
    예외가 발생할 만한 코드
except:
    예외가 발생했을 때 처리할 코드
'''
'''
print('[예외 처리를 하지 않은 경우]')
#숫자가 아닌거 입력시:ValueError: invalid literal for int() with base 10: 'sfdsgf'
years = int(input('나이를 입력하세요?'))
print('당신의 10년후 나이는',years+10)
'''
print('[예외 처리를 한 경우]')
try:
    years = int(input('나이를 입력하세요?'))
    print('당신의 10년후 나이는',years+10)
#except:
#    print('나이는 숫자만...')
except ValueError as e:
    print('나이는 숫자만...',e)
