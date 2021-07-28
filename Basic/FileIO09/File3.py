#read()함수 - 파일 전체 내용을 읽는다
#파일이 없는 경우:FileNotFoundError
print('[read()함수]')
try:
    with open('line.txt','r',encoding='utf8') as f:
        print(f.read())
        #print(f.read(10))#10은 글자 수 즉 10자만 읽는다
        print(f.newlines)#줄바꿈 출력됨
except Exception as e:
    print('파일 읽기 오류:',e)
#read()함수 - 파일 전체 내용을 읽어 리스트로 변환하기
with open('line.txt','r',encoding='utf8') as f:

    #list_=f.read().split('\n')#마지막 요소에 빈 문자열이 포함됨
    #print(list_)#['파일쓰기 시작!!!', '1번째 라인 입니다', '2번째 라인 입니다', '3번째 라인 입니다', '4번째 라인 입니다', '5번째 라인 입니다', '6번째 라인 입니다', '7번째 라인 입니다', '8번째 라인 입니다', '9번째 라인 입니다', '10번째 라인 입니다', '파일쓰기 끝!!!', '']
    #[마지막 요소 ''  제거하기]
    #읽어온 문자열을 양쪽 공백제거후 split
    #list_ = f.read().strip().split('\n')
    #print(list_)
    #슬라이싱 사용
    #list_ = f.read().split('\n')[:-1]
    #print(list_)
    #표준함수인 filter(함수,반복가능한 객체)함수 사용해서 ''제거하기
    # filter에 전달하는 함수는 True나 False를 반환하는 함수여야 True인 요소만 필터링된다
    list_ = f.read().split('\n')
    list_ = list(filter(lambda s : s != '',list_))
    print(list_)
#readline()함수: 한 라인씩 읽은 함수.파일의 끝에 도달하면 empty string반환
print('[readline()함수]')
with open('line.txt','r',encoding='utf8') as f:
    #print(f.readline())#첫번째 라인만 읽는다
    print(f.readline(5))#첫번째 라인에서 5글자만 읽는다
#모든 라인을 읽어 보자
with open('line.txt','r',encoding='utf8') as f:
    while True:
        line = f.readline()
        if len(line)==0:
            break
        print(line,end='')
#readlines():파일의 모든 라인을 한꺼번에 읽어서 각각의 라인(줄)을
#요소로 갖는 리스트로 반환
print('[readlines()함수]')
with open('line.txt','r',encoding='utf8') as f:
    lines = f.readlines()
    #print(lines)#리스트의 각 요소인 str에 \n이 포함됨
    #아래는 \n제거
    #print(list(map(lambda s : s[:-1],lines)))
    print(list(map(lambda s: s.replace('\n',''), lines)))