import scrapy #1.scrapy import
'''
    요소찾기:
    response객체(HtmlResponse)의 xpath([/text()]) 혹은 css([::text]) :[<Selector/>,<Selector/>...]반환
    Selector객체의 xpath() 혹은 css()메소드로 찾는다

    단,response객체의 xpath() 혹은 css() 메소드에 text() 혹은 ::text를
    넣으냐 넣지 않느냐에 따라 
    텍스트 추출시
    Selector객체의 xpath().extract() 혹은 css().extract()메소드의 반환타입이 달라진다
    extract():Selector객체의 data속성 추출시 호출
'''
class BasicXpathSpider(scrapy.Spider):#2.scrapy.Spider 상속
    name = 'css_spider'
    def start_requests(self):#3.start_requests()오버라이딩
        urls=['https://news.naver.com/']
        for url in urls:

            yield scrapy.Request(url=url,callback=self.parse)

    def parse(self, response, **kwargs):#4.오버라이딩
        '''
        HtmlResponse객체의 css('CSS SELECTOR')메소드: SelectorList반환 즉
                                                    [<Selector xpath='xpath문법' data='추출한 요소(태그)'/>,....]

        ※CSS SELECTOR로 찾은 경우 다시 XPATH로 변환이 된다
         즉 XPATH로 찾는 것이 유리하다
        '''
        self.log('[response객체의 타입]')
        self.log('response객체의 타입:'+str(type(response)))
        self.log('[response객체의 url속성]')
        self.log('요청한 URL:'+response.url)
        self.log('[response객체의 text]')
        #self.log(response.text)
        #settings.py의 ROBOTSTXT_OBEY = False로 변경후
        #(crawling) E:\CCH\Workspace\python\Crawling\scrapy04\basicbot>scrapy crawl css_spider
        #scrapy crawl 스파이더이름
        selectors=response.css('#today_main_news > div.hdline_news > ul > li > div.hdline_article_tit > a::text')
        #selectors:SelectorList타입
        self.log('[selctors객체 출력]')
        self.log(selectors)
        '''
        [<Selector xpath='위 CSS SELECTOR가 XPATH로 바꾼 경로'   data='\n   ...'>, 
         <Selector xpath='위 CSS SELECTOR가 XPATH로 바꾼 경로'   data='\n   ...'> ]
        '''
        self.log('[Selector객체 첫번째 요소 출력]')
        selector = selectors[0]
        self.log(message='value:{},type:{}'.format(selector,type(selector)))
        #Selector의 data속성 추출:extract()
        self.log('[찾은 요소 a태그의 텍스트 스크래핑]')
        text = selector.extract()
        self.log(message='value:{},type:{}'.format(text.strip(), type(text)))
        self.log('[모든 헤드라인 뉴스 제목 스크래핑]')
        for selector in selectors:
            self.log(selector.extract().strip())
