import scrapy

class BasicXpathSpider(scrapy.Spider):
    name = 'xpath_spider'

    def start_requests(self):
        urls = ['https://news.naver.com/']
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response, **kwargs):
        '''
        HtmlResponse객체의 xpath('xpath문법')메소드: SelectorList반환 즉
        [<Selector xpath='xpath문법' data='추출한 요소(태그)'/>,....]
        '''
        selectors=response.xpath('//*[@id="today_main_news"]/div[2]/ul/li/div[1]/a/text()')
        # selectors:SelectorList타입
        self.log('[selctors객체 출력]')
        self.log(selectors)
        '''
        [<Selector xpath='위 CSS SELECTOR가 XPATH로 바꾼 경로'   data='\n   ...'>, 
         <Selector xpath='위 CSS SELECTOR가 XPATH로 바꾼 경로'   data='\n   ...'> ]
        '''
        self.log('[Selector객체 첫번째 요소 출력]')
        selector = selectors[0]
        self.log(message='value:{},type:{}'.format(selector, type(selector)))
        # Selector의 data속성 추출:extract()
        self.log('[찾은 요소 a태그의 텍스트 스크래핑]')
        text = selector.extract()
        self.log(message='value:{},type:{}'.format(text.strip(), type(text)))
        self.log('[모든 헤드라인 뉴스 제목 스크래핑]')
        for selector in selectors:
            self.log(selector.extract().strip())