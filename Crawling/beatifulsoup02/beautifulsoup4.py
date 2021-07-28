#쿠팡 상품 목록 정보 가져오기(함수버전)
import requests
from bs4 import BeautifulSoup

def createUrl(pageNumber):
    pages = []
    searchProduct=input('검색하려는 단어를 입력하세요?')
    for page in range(1,pageNumber+1):
        url='https://www.coupang.com/np/search?q={}&page={}'.format(searchProduct,page)
        pages.append(url)

    return pages

def scrapping(urls):#yield키워드를 사용해서 반환하는 함수:제너레이터-이터레이터를 생성
    for url in urls:
        # 1. HTML소스 가져오기
        res = requests.get(url, headers={'User-agent': 'Mozilla/5.0'})

        # 2. HTML소스에서 BeautifulSoup로 원하는 데이타(상품명하고 가격) 가져오기
        soup = BeautifulSoup(res.text, 'html.parser')
        # 상품명
        names = soup.select(selector='#productList>li > a > dl > dd > div > div.name')

        # 가격
        prices = soup.select('#productList>li > a > dl > dd > div > div.price-area > div.price-wrap > div.price > em > strong')
        print('yiled하기')
        yield zip(names,prices)

if __name__=='__main__':
    pageNumbers = int(input('페이지 번호를 입력하세요?'))
    urls=createUrl(3)
    print('scrapping호출 전')
    products=scrapping(urls)
    print('scrapping호출 후')
    list_ =list(products)

    for i in range(len(list_)):
        print('[{} 페이지 상품 목록 입니다]'.format(i + 1))
        for name, price in list_[i]:
            print('상품명 : {}'.format(name.text))
            print('가  격 : {}'.format(price.text))
            print('-'* 50)



