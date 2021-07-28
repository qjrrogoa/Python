import bs4
from bs4 import BeautifulSoup
import re
html_doc = """
<html><head><title>The Dormouse's story</title></head>
<body>
    
    <p class="title"><b>The Dormouse's story</b></p>

    <p class="story">Once upon a time there were three little sisters; and their names were
        <a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
    <a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
    <a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

    <p class="story">...</p>
"""
soup = BeautifulSoup(html_doc,'html.parser')
print('[soup인스턴스의 이름공간]')
print(dir(soup))
print('[HTML소스를 인덴트해서 예쁘게 출력:prettify()]')
#print(soup.__str__)#print(soup)
print(soup.prettify())
#soup.HTML태그명(소문자) :제일 먼저 발견되는 태그  요소 하나(<class 'bs4.element.Tag'>)
#                    없으면 None
print('[최초로 발견되는 태그 요소 하나(one)찾기]')
print('1.soup.HTML태그명(소문자)')
print(soup.a,type(soup.a))#str아니라 <class 'bs4.element.Tag'>객체다
tag = soup.a
print('2.soup.find("HTML태그명(소문자)")')
print(soup.find('a'),type(soup.find('a')))
print('[Tag타입의 이름공간]')
print(dir(tag))
print('[Tag타입의 주요 메소드 및 속성]')
print('A. 태그명 : name속성')
print(tag.name)
print('B. 시작태그와 종료태그 사이의 텍스트:string/text속성 혹은 get_text()메소드')
#string :텍스트가 없는 경우 None
#text :텍스트가 없는 경우 ''
#get_text():텍스트가 없는 경우 ''
print('string:{},text:{},get_text():{}'.format(tag.string ,tag.text,tag.get_text()))
print('[특정 태그명에 해당하는 모든 태그 요소 찾기]')
#soup('태그명')
#혹은 soup.find_all('태그명')
#반환값은 무조건 리스트를 상속받은 ResultSet
#찾는 태그가 없으면 빈 ResultSet([])를 반환
#즉 [Tag객체,Tag객체2,......]
print('1. soup("HTML태그명"))')
tags = soup('a')
print(tags,type(tags))#리스트가 아니라 <class 'bs4.element.ResultSet'>타입
print('2. soup.find_all("HTML태그명")')
tags = soup.find_all('a')
print(tags,type(tags))
print('2-1.원하는 갯수의 태그만 가져오기: soup.find_all("HTML태그명",limit=숫자)')
tags = soup.find_all('a',limit=2)
print(tags,type(tags))
print('[모든 a태그의 텍스트 얻기]')
for tag in soup.find_all('a'):
    print(tag.text)
print('[텍스트에서 특정 문자열 찾기 - 문자열로 찾기(정확히 문자열이 일치해야함)]')
rs=soup.find_all(string="The Dormouse's story")#모든 태그의 텍스트에서 The Dormouse's story문자열 찾기
print(rs)#ResultSet타입의 각 요소는 <class 'bs4.element.NavigableString'>
print(isinstance(rs[0],str))
print('[텍스트에서 특정 문자열 찾기 - 정규표현식으로 찾기]')
rs = soup.find_all(string=re.compile('.+ie'))
print(rs)
print('[특정 태그의 속성값 가져오기] ')
'''
soup.태그명['속성명']
soup.태그명.get('속성명')
soup.태그명.attrs['속성명']
즉 Tag객체['속성명'],혹은 Tag객체.get('속성명') 혹은 Tag객체.attrs['속성명']
'''
#soup.태그명
print('[href속성값 가져오기]')
print(soup.a['href'])#속성명이 없을때 KeyError발생
print(soup.a.get('href'))#속성명이 없을때 None
print(soup.a.attrs['href'])#속성명이 없을때 KeyError발생
#태그객체
print(tag['href'],tag.get('href'),tag.attrs['href'], sep=' | ')
print(type(soup.a['href']))#<class 'str'>
print('[모든 특정 태그의 속성값 가져오기]')
for tag in soup.find_all('a'):
    print(tag['href'],tag['class'],tag['id'],sep= ' | ')

print('[id속성으로 태그 객체 가져오기]')
'''
soup.find(id="아이디명")
soup.find(None,{'id':'아이디명'})
'''
print(soup.find(id='link1'),soup.find(None,attrs={'id':'link1'}),sep=' | ')
print('[class속성으로 태그 객체 가져오기]')
'''
soup.find_all(class_="클래스명")#class는 파이썬의 예약어 그래서 class_사용
soup.find_all(None,{'class':'클래스명'})
'''
sisters = soup.find_all(class_ = 'sister')
sisters = soup.find_all(None,{'class':'sister'})
print(sisters)
print('[CSS셀렉터로 태그 가져오기]')
'''
select('CSS셀렉터'):find_all()과 같다
select_one('CSS셀렉터'):find()와 같다
'''
selector = soup.select('p > a')
print(selector,type(selector))
for tag in selector:
    print(tag.text)
selector = soup.select_one('p > a')
print(selector,type(selector))
print(selector.text)


















