'''
-Spider클래스  및 Item Pipeline을 위한 클래스 작성
 웹 사이트의 페이지 정보룰 JSON형태 및 CSV로 추출해서
 Command Line을 이용해 JSON과 CSV파일이로 저장하거나
 Item Pipeline을 통해 파일로 저장하는 스파이더

대상 사이트:http://wowpro.wownet.co.kr의 탑메뉴 증권방송 -> 종목동영상
사용한 API:
    start_urls 클래스 속성 사용(리스트 형태의 목록으로,
    각 URL 요청을 보내도록 start_requests(self)이 자동으로 구현이 된다.
    즉 start_requests(self)를 오버라이딩 할 필요 없다)
    start_requests(self)는 사용 불필요
    parse(self, response)메소드 구현
    parse(self, response)메소드에서 Item Pipeline(pipelines.py에 정의한 클래스)에 item을 전달
'''
#1.scrapy import
import scrapy
#2.scrapy.Spider 상속받은 클래스 작성(Spider)
class WownetSpider(scrapy.Spider):
    # 3.클래스 속성인 name변수에 식별자 할당
    name = 'wownet_2'
    # 4.특정 URL로 요청을 보내기 위한 start_urls 클래스 속성에 URL할당
    # start_requests(self) 오버라이딩 불필요
    start_urls=[
            'https://www.wownet.co.kr/StockBrdCstIng/StockBrdCstIngInfo/WowNetTvItemList?page=1',
            'https://www.wownet.co.kr/StockBrdCstIng/StockBrdCstIngInfo/WowNetTvItemList?page=2']

    # 5.응답을 처리할 parse()메소드 오버라이딩
    def parse(self, response, **kwargs):
        # Response객체의 주요 메소드
        # css('CSS셀렉터') : SelectorList라는 list형태의 객체반환.SelectorList는 Selector객체들을 저장하고 있다
        # xpath('XPATH표현식') :SelectorList라는 list형태의 객체반환. 매우 강력한 데이타 추출 메소드로 Scapy Selector의 근간이다.
        # 사실 CSS 셀렉터를 이용한 추출도 XPATH로 변환이 되어 추출이 된다
        # follow('상대경로',callback='파싱함수') : 상대경로를 지원하는 함수로 첫번째 인자로 a태그의 href속성에서 추출한
        # 상대경로를 넣어주면 전체 경로로 변환된다.scrapy.Request('절대경로',callback='파싱함수')함수 대신사용할 수 있다
        # Selector객체의 주요 메소드
        # Selector(text='문자열') :문자열을 Selector객체로 반환하는 생성자
        # 아래는 텍스트 데이타를 추출하기위한 함수들이다
        # extract() : list형태 정보 반환.찾는 요소가 없으면 []반환
        #
        #             SelectorList객체[0].extract() 이면 str반환
        #             SelectorList객체.extract()면 list반환
        # extract_first(): 리스트의 첫번째 아이템 반환.찾는 요소가 없으면 None반환
        # 아래 메소드는 최신버전의 scrapy의 API
        # get() : 찾는 텍스트 요소중 첫번째 반환(반환타입 str).extract_first()와 같다
        # getall() : 모든 요소를 리스트로 반환(반환타입이 무조건 list).extract()와 유사

        # ※유니코드를 한글로 변환하기위해
        # settings.py에 FEED_EXPORT_ENCODING='utf-8'추가
        # 스크래핑한 데이타를 파일로 저장할때는 현재 메소드에서 yield하자
        # 방법1]커맨드 창에서 명령어로 JSON/CSV파일로 만들기-Item Pipeline을 위한 클래스 작성 불필요
        # (crawling) E:\CCH\Workspace\python\Crawling\scrapy04\wownetbot>scrapy crawl wownet_2 -o wownet.json(csv로 저장시에는 -o wownet.csv)

        # 방법2]ItemPipeline 용 클래스 작성해서 JSON/CSV파일로 만들기-Item Pipeline을 위한 클래스 작성(pipelines.py수정)
        # pipelines.py에 클래스(아이템 파이프라인) 작성후 settings.py에  반드시 pipeline설정
        # 예]ITEM_PIPELINES = {'wownetbot.pipelines.WownetbotJSONPipeline': 300,}
        # Spider 실행시 -o 옵션 제거
        #(crawling) E:\CCH\Workspace\python\Crawling\scrapy04\wownetbot>scrapy crawl wownet_2
        selectors=response.xpath('//*[@class="videoList"]/li')
        self.log('[selectors]\n{}\n총 요소 갯수:{}'.format(selectors,len(selectors)))

        #필요한 데이타 추출
        for selector in selectors:
            #이미지 경로 추출
            src=selector.xpath('figure/img/@src').get()
            title= selector.xpath('ul/li[1]/text()').get()
            date = selector.xpath('ul/li[2]/text()').get()
            item={'src':src,'title':title,'date':date}
            self.log(item)
            # This method(parse)  must return an iterable of Request and/or dicts or Item objects.
            #CSV로 저장시에는 키값들이 csv파일의 헤더가 된다
            yield item#Item Pipeline(pipelines.py에 정의한 클래스)에 item을 전달


