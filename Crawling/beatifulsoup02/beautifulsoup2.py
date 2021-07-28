#네이버 환율 정보 가져오기(스크래핑 하기)
import requests #HTML소스 전체 스크래핑용
from bs4 import BeautifulSoup #HTML소스에서 원하는 데이타 스크래핑용
#네이버에서 네이버 환율로 검색후 사이트 주소 복사
url='https://finance.naver.com/marketindex/'
res=requests.get(url)
print(res.text)#HTML소스
htmlSource = res.text
#BeautifulSoup로 스크래핑 하자
soup = BeautifulSoup(htmlSource,features='html.parser')
dollar=soup.select_one(selector='#exchangeList > li.on > a.head.usd > div > span.value')
print('1달러 완율:',dollar.text)
yen = soup.select_one('#exchangeList > li > a.head.jpy > div > span.value')
print('100엔 환율:',yen.text)
