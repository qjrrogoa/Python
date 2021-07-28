#리스트의 요소들을 파일에 쓰기:writelines()
#리스트
lines =['한국 소프트웨어','인재 개발원입니다','파이썬 수업입니다','자바보다 쉬워요','화이팅!!!',2021]
#with절 미 사용-write(str)함수 사용
f=open('list.txt','wt',encoding='utf-8')

'''
아래는 메소드
readable : 읽기 가능 여부 .읽기 가능시 True 아니면 False
writable : 쓰기 가능 여부 .쓰기 가능시 True 아니면 False
파일객체 관련 속성:
closed : 파일객체가 닫혀 있으면 True,아니면 False
encoding : 파일 인코딩 설정 값
mode : mode설정 값
name : 파일명
newlines : 파일객체가 가리키는 파일내용에서 줄바꿈이 있는 경우 그 줄바꿈 문자 반환
'''
print('[파일객체의 주요 속성 출력]')
print('readable():',f.readable())
print('writable():',f.writable())
print('closed:',f.closed)
print('encoding:',f.encoding)
print('mode:',f.mode)
print('name:',f.name)
print('newlines:',f.newlines)
#write(str객체)
#f.write(lines)#TypeError: write() argument must be str, not list 즉 인자는 무조건 str
#write()함수를 사용해 리스트의 요소를 파일로 출력
'''
for element in lines:
    f.write(str(element)+'\n')
f.close()
'''
#writelines(반복가능한객체) 함수 사용.반복가능한 객체의 요소는 모두 str이어야 한다
#f.writelines(lines)#TypeError: write() argument must be str, not int
f.writelines(map(lambda s : s+'\n',map(str,lines)))
f.close()

#with절 사용-close() 불필요
with open('list_with.txt','wt',encoding='utf-8') as f:
    f.writelines(map(lambda s: s + '\n', map(str, lines)))

