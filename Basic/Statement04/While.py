#1부터 10까지 누적합:while문 사용
sum =0
i = 1#초기식
while i <=10:#반복 조건
    sum+=i#실행문
    i+=1#증감식
print('1부터 10까지 누적합',sum,sep=":")
'''
문]1부터 1000까지 숫자중 3의 배수 이거나 5의 배수인
숫자의 합을 구해라
단, 3과5의 공배수인 경우 제외(while문 사용)
'''
sum =0
i=1
while i <=1000:
    if (i%3==0) ^ (i%5==0):
        sum+=i
    i+=1
print('1부터 1000까지 3과 5의 배수의 누적합(공배수 제외)',sum,sep=":")
#반복할 횟수가 정해지지 않은 경우 while문 사용
import random
i =1
while i !=5:
    i = random.randint(1,10)#1부터 10까지 난수 발생
    print('i는',i)
'''
* 1 0 0 0
* 0 1 0 0
* 0 0 1 0
* 0 0 0 1  while문으로...
'''
i=1#바깥 WHILE의 초기식
k=1#안쪽while의 초기식
while i < 5:#바깥 while문(행)
    while k < 5:#안쪽 while(열)
        if k==i:
            print('%-2d' % 1,end="")
        else:
            print('%-2d' % 0, end="")
        k+=1#안쪽 while의 증가식
    k=1#k를 다시 1로 초기화:
    i+=1#바깥 while의 증감식
    print()#줄바꿈
'''

* 
* *
* * *
* * * *
* * * * *(while문으로)
'''
k=1
while k <=5:
    j=1
    while k >=j:
        print('%-2c' % '*',end="")
        j+=1
    print()
    k+=1
'''
문]아래 형식대로 구구단을 출력
2 * 1 = 2   3 * 1 = 3   4 * 1 = 4........9 * 1 = 9
2 * 2 = 4   3 * 2 = 6   4 * 2 = 8........9 * 2 =18
..
..
2 * 9 = 18  3 * 9 = 27  4 * 9 =36....... 9 * 9 = 1  
while문으로...
'''
i=1
while i<=9:
    k=2
    while k<=9:
        print('%-2s * %-2s = %-4s' % (k,i,k*i),end='')
        k+=1
    print()
    i+=1
#무한 반복
while True:
    print('HELLO')

print('프로그램 끝!!!')#자바처럼 UnReacgable Code Error가 발생하지 않는다

