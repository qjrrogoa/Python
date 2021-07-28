#스파이더 첫번째
'''
-Spider클래스만 작성해서 웹 사이트의 페이지를 .html로 저장하는 스파이더

대상 사이트:http://wowpro.wownet.co.kr의 탑메뉴 증권방송 -> 종목동영상
사용한 API:
    start_urls 클래스 속성 미 사용
    start_requests(self): 메소드 및 parse(self, response)메소드 구현

    parse(self, response)메소드에서 Item Pipeline(items.py에 정의한 클래스)에
    item을 미 전달
'''
# 1.scrapy import
import scrapy
#2. scrapy.Spider 상속을 상속한 클래스 작성(스파이더)
class WownetSpider(scrapy.Spider):
    # 3.클래스 속성인 name변수에 식별자 할당
    name = 'wownet_1'#Spider 식별자로 프로젝트내에서는 유일해야 한다
                     # CLI로 실행시 scrapy crawl wownet01
    #4.특정 URL로 요청을 보내기 위한 start_requests()메소드 오버라이딩
    def start_requests(self):
        urls=[
            'https://www.wownet.co.kr/StockBrdCstIng/StockBrdCstIngInfo/WowNetTvItemList?page=1',
            'https://www.wownet.co.kr/StockBrdCstIng/StockBrdCstIngInfo/WowNetTvItemList?page=2']
        for url in urls:
            # 방법1
            # url은 요청주소,callback은 응답을 처리할 메소드 설정
            yield scrapy.Request(url,self.parse)

    # 5.응답을 처리할 parse()메소드 오버라이딩
    # 요청한 서버로부터 응답을 받으면 자동으로 호출되는 콜백메소드
    # URL의 각 요청을 처리하는데 사용하는 메소드로 명시적으로 호출하지 않아도
    # 각 요청에 대해 자동으로 호출되는 Scrapy의 디폴트 콜백 메소드
    def parse(self, response, **kwargs):
        #response: URL요청에 대한 Response객체(HtmlResponse)
        #response객체의 주요 속성
        # url : 요청한 URL(문자열)
        # text : HTML소스
        # status : 응답 상태 코드(숫자).기본값 200
        # headers:응답헤더(dict)
        # body : 응답바디.str로 디코딩된 텍스트(파이썬 2에서는 유니코드)
        self.log('[요청한 사이트 URL]')
        self.log(response.url)
        self.log('[응답 코드]')
        self.log(response.status)
        self.log('[응답 헤더]')
        self.log(response.headers)
        #self.log('[응답 바디]')
        #self.log(response.body.decode('utf8'))
        # 페이지번호를 사용해서 .html파일명 만들기
        pageNo = response.url[-1]
        fileName = 'wownet-{}.html'.format(pageNo)
        #response.text 사용 : 요청한 주소의 전체 HTML소스를 .HTML파일로 저장
        with open(fileName,'w',encoding='utf8') as f:
            f.write(response.text)

        self.log('{}파일명으로 저장되었습니다'.format(fileName))



