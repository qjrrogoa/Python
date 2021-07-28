#대소문자 엄격 구분
#자료형 선언이 없다
#a#NameError: name 'a' is not defined
a=10
print(a)
a="문자열입니다"
print(a)
#한 라인에 여러개 명령어 작성시에는 마지막 명령을 제외한 명령어에는 ; 을 붙인다
b=20;c=a+str(b);print(c)
#파이썬은 들여쓰기가 문법이다
for i in range(5):
#print(i)#IndentationError: expected an indented block
    #print(i)
    pass
print("i는 %d" % i)
if b % 2 == 0 :
    print("짝수:",end="")
    print(b)
else:
    print('홀수:',b)