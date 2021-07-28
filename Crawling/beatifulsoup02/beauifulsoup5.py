import requests
from bs4 import BeautifulSoup

#위키피디아에서 윤동주 작품
#아래처럼 수집하기
"""
《새 명동》
《서시(序詩)》
《또 다른 고향》
《별 헤는 밤》
《하늘과 바람과 별과 시》
《사진판 윤동주 자필 시고전집》
《별을 사랑하
"""
res = requests.get('https://ko.wikipedia.org/wiki/윤동주')
soup = BeautifulSoup(res.text,'html.parser')
works=soup.select('#mw-content-text > div.mw-parser-output > ul:nth-child(50) > li')
print(works)#[Tag,Tag,.....]
for work in works:
    #print(work.text)
    aTag=work.find('a')
    #print(aTag)
    if aTag:
        print('《{}》'.format(aTag.text))
    else:
        print(work.text)
