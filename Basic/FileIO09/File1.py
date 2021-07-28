#with절 미 사용
#쓰기모드로 파일 열기.파일형식은 텍스트모드:파일이 없으면 파일이 생성됨.
#기존 파일이 존재하는 경우 기존 내용은 없어짐
#문자열을 파일에 쓰기
'''
try:
    f=open('line.txt','w',encoding='utf8')#wt모드로 파일 열기.기본이 텍스트 모드임
    print('value:{},type:{}'.format(f,type(f)))
    print(dir(f))
    f.write('파일쓰기 시작!!!\n')#파일에 문자열 쓰기
    for i in range(1,11):
        textLine = '{}번째 라인 입니다\n'.format(i)
        f.write(textLine)
    f.write('파일쓰기 끝!!!\n')
    #f.read()#파일을 쓰기 전용모드로 열었기때문에 io.UnsupportedOperation: not readable 발생
    print(f.readable())
    print('[파일읽기 모드로 변경후 파일 내용 전체 읽기]')
    f = open('line.txt','r',encoding='utf8')
    print(f.read())
except Exception as e:
    print('쓰기모드로 파일 열기 실패 혹은 파일 쓰기 오류:',e)
finally:
    f.close()#파일 객체 닫기
'''
#with절 사용 :※ with구문은 파이썬 2.5부터 지원
#파일객체를 close()불 필요. 자동으로 close()됨(finally절 불필요)
try:
    with open('line.txt','w',encoding='utf8') as f: 
        f.write('파일쓰기 시작!!!\n')#파일에 문자열 쓰기
        for i in range(1,11):
            textLine = '{}번째 라인 입니다\n'.format(i)
            f.write(textLine)
        f.write('파일쓰기 끝!!!\n')
except Exception as e:
    print('파일 IO 오류 발생:',e)
