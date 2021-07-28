#쿠팡 상품 목록 정보 가져오기
import requests
from bs4 import BeautifulSoup

searchProduct=input('검색하려는 단어를 입력하세요?')
url='https://www.coupang.com/np/search?q={}'.format(searchProduct)
#1. HTML소스 가져오기
res=requests.get(url,headers={'User-agent':'Mozilla/5.0'})
print(res.text)
#2. HTML소스에서 BeautifulSoup로 원하는 데이타(상품명하고 가격) 가져오기
soup = BeautifulSoup(res.text,'html.parser')
#상품명
names = soup.select(selector='#productList>li > a > dl > dd > div > div.name')
print(names)
#가격
prices = soup.select('#productList>li > a > dl > dd > div > div.price-area > div.price-wrap > div.price > em > strong')
print(prices)
print(len(names),len(prices))
#상품명하고 상품가격을 튜플로 묶는다:zip(*iteratable)함수
#튜플을 언패킹해서 name과 price에 상품명하고 가격을 담자
print(list(zip(names,prices)))
for name,price in zip(names,prices):
    print('{} : \\{}원'.format(name.text,price.text))

