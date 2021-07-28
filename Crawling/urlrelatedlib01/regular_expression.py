'''
[패턴을 표현하는 문자]

. : 임의의 한글자를 의미
예) a.b(acb,afb........)
*  :  * 바로 앞의 문자가 없거나 한 개 이상이 있을 경우
예) a*b (b,ab,aab,aaab....)
+ : +바로 앞의 문자가 최소 한개 이상일때
예) a+b (ab,aab,aaab...)
? : ?바로 앞의 문자가 없거나 한 개 존재하는 경우
예) a?b (b,ab,)
^ : ^ 뒤에 문자열과 같은 문자열로 시작하는 경우
      즉 문자열의 시작을 의미
    [ ]안에서 ^ 는 [ ]안의 문자를 제외한 문자를 의미
예) ^ab(ab,abc,abdr...)
$ : $앞의 문자열과 같은 문자열로 끝나는 경우 즉 문자열의 끝을 의미
예) ab$ (avab,aab,abab...)

[] : []안에 문자열중에 하나만의 문자만을 의미
예) [a-z](a부터 z까지중 한 문자)
    [0-9](0부터 9까지 숫자중 한 문자)
 [abc](a혹은 b혹은 c)

{} :{}앞의 문자열의 개수를 의미 문자{최소개수,최대개수}
    최소개수는 반드시 있어야하고 최대개수가 없는경우는 1개또는 1개이상을 의미
 하고 숫자 하나만을 적어 주엇을때는 그 숫자만큼의 개수를 의미한다.

예) abc{1,2} (abc,abcc)
    a{3} (aaa)
 a{1,} (a,aa,aaa....)

 | : or 연산자

 [^ ] : []안의 문자는 사용 못한다는 의미

예) [^abc] (a나 b나 혹은 c를 포함하지 않은 한 문자)
    [^0-9] (0에서 9까지의 숫자를 포함하지 않은 한 문자)
\s	공백 문자
\S	공백 문자가 아닌 나머지 문자
\w	알파벳이나 숫자
\W	알파벳이나 숫자를 제외한 문자
\d	숫자 [0-9]와 동일
\D	숫자를 제외한 모든 문자
'''
import re #정규 표현식 라이브러리

#email = 'kim@nave.com'
email='kim.naver.com'
pattern=re.compile("[a-zA-Z]+@\\w+\\.[a-zA-Z]+")
match=pattern.match(email)#이메일 주소가 패턴에 맞는지 비교하기 위한 Match객체 생성
if match:
    print('이메일 형식입니다')
else:
    print('이메일 형식이 아닙니다')


log="[17.07.11 23:29:11] [INFO ]  [eclipse.galileo-bean-thread-50618297 galileo.site.SiteBean:317 ] - ##galileo_bean end. MessageExchange_ID:ID:localhost-15a6308ba1c-6:86071562";
print(len(log))
#log="--------------------------------------------"
#1.패턴 객체 생성
pattern=re.compile("\\[(\\d{2}\\.\\d{2}\\.\\d{2}\\s\\d{2}:\\d{2}:\\d{2})\\]\\s\\[(.+)\\]\\s\\s\\[(.+)\\]\\s-\\s(.+)")
print('value:{},type:{}'.format(pattern,type(pattern)))
#2.패턴 객체의 match('패턴을 검사할 문자열')메소드로 Match객체 생성
#  패턴이 일치하면 Match객체 반환 불일치시 None반환
match = pattern.match(log)
print('value:{},type:{}'.format(match,type(match)))
if match:
    print(len(match.groups()))
    print('매치가 시작된 인덱스:',match.start())
    print('매치가 끝나는 인덱스:', match.end())
    for index in range(len(match.groups())+1):#0번이 매칭된 전체 문자열임으로 마지막방은 +1
        print(match.group(index))




