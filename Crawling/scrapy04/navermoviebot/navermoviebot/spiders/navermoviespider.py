import scrapy
#스크래핑한 데이타를 담을 NavermoviebotItem import

#현재 Crawling폴더가 프로젝트 root로 되어있는거를 navermoviebot폴더를
#프로젝트 root로 변경한다
#프로젝트 폴더(navermoviebot) 선택 후  Mark Directory as->Sources Root선택
from navermoviebot.items import NavermoviebotItem

#크롤링 및 스크래핑할 규칙을 정의할 클래스(스파이더)
#robots.txt 규칙을 따르지 않겠다고 False로 설정
#ROBOTSTXT_OBEY = False
#2.scrapy.Spider상속
class NaverMovieSpider(scrapy.Spider):
    # 3. name 클래스속성 지정
    name = 'naver_movie'
    # 4.start_urls 클래스 속성을 사용하거나 start_request()메소드 오버라이딩
    # 네이버 영화 > 영화랭킹
    start_urls=['https://movie.naver.com/movie/sdb/rank/rmovie.naver']



    # 5. parse()오버라이딩(크롤링 및 스크래핑 규칙 정의):start_urls에 지정한 url요청시 응답을 받았을때 자동 호출
    def parse(self, response, **kwargs):
        # 조회순,평점순등의 링크주소 즉 URL 스크래핑하기
        hrefs = response.xpath('//*[@id="old_content"]/div[1]/ul/li/a/@href').getall()
        self.log('[링크 주소]:{}'.format(hrefs))
        for href in hrefs:
            #Request객체로 요청을 보내기
            # 방법1:yield scrapy.Request('절대경로')  callback 생략시 디폴트로 parse()메소드 호출됨
            #url=response.urljoin(href)#상대경로를 인자로 전달하면 절대경로 반환
            #self.log('[절대 경로]:{}'.format(url))
            #yield scrapy.Request(url)#혹은 yield scrapy.Request(url,callback=parse)
            # 방법2:reponse.follow('상대경로',callback=self.임의의파싱함수)
            request=response.follow(href,callback=self.parseMovieRank)
            self.log('value:{} | type:{}'.format(request,type(request)))#<class 'scrapy.http.request.Request'>
            yield request#조회순,평점순(현),평점순(모) URL 요청

    def parseMovieRank(self,response):#조회순,평점순(현),평점순(모) URL 요청시 응답을 받았을때 자동 호출
        #순위,영화 제목 스크래핑(1등부터 10등까지 가져오기(첫번째 행은 빈 공백))
        rows=response.xpath('//*[@id="old_content"]/table/tbody/tr')[1:11]
        self.log('[tableRows]\n{}\n영화 갯수:{}'.format(rows,len(rows)))
        for row in rows:
            # 스크래핑할 데이타를 담을 Item클래스 생성
            item=NavermoviebotItem()#한편의 영화 저장용


            #영화랭킹 메뉴 저장
            if response.url.find('sel=cnt') != -1:
                item['rankingMenu']='조회순'
            elif response.url.find('sel=cur') != -1:
                item['rankingMenu'] = '평점순(현재상영영화)'
            else:
                item['rankingMenu'] = '평점순(모든영화)'
            #순위 저장
            item['rank'] = row.xpath('td[1]/img').attrib['alt']#혹은 row.xpath('td[1]/img/@alt').get()
            # 영화제목
            item['movieTitle'] = row.xpath('td[2]/div/a/text()').get()
            # 영화제목 링크로 요청을 보내기 위해 링크 주소 스크래핑
            movieTitleLink = response.urljoin(row.xpath('td[2]/div/a/@href').get())
            #※조회순, 평점순등의 순위에서  영화가 동일한 경우 스파이더는 동일한 URL에 대해서
            #기본적으로 한번밖에 요청하지 않는다(DEBUG: Filtered duplicate request).이를 해결하기위해서 dont_filter = True를 추가하면
            #동일한 URL에 대해서도 다시 요청한다.
            request = scrapy.Request(movieTitleLink,callback=self.parseMovieDetail,method='GET',dont_filter=True)

            # parseMovieDetail()메소드로 item을 전달하기(나머지 필드(상세정보 저장용)를 스크래핑한 값으로 설정하기 위해)
            # Request객체의 meta속성에 item 저장후 yield




            request.meta['item'] = item
            yield request

    # 해당 영화 상세페이지 파싱하는 메소드
    def parseMovieDetail(self,response):
        #parseMovieRank메소드에서 전달한 Item객제 가져오기
        item=response.meta['item']
        #감독
        item['director']=response.xpath('//*[@id="content"]/div[1]/div[2]/div[1]/dl/dd[2]/p/a/text()').get().strip()
        #장르
        item['genre']=','.join(response.xpath('//*[@id="content"]/div[1]/div[2]/div[1]/dl/dd[1]/p/span[1]/a/text()').getall()).strip()
        # 관람객 평점
        item['visitorScore']=response.xpath('//*[@id="actualPointPersentBasic"]/div/span/span/text()').get().strip()
        # 네티즌 평점
        item['netizenScore'] ='네티즌 평점 '+ response.xpath('//*[@id="pointNetizenPersentBasic"]/span/span/@style').get()[6:-1]+'점'
        # 국가
        item['nationality']=','.join(response.xpath('//*[@id="content"]/div[1]/div[2]/div[1]/dl/dd[1]/p/span[2]/a/text()').getall()).strip()
        # 상영시간
        item['showtimes']=response.xpath('//*[@id="content"]/div[1]/div[2]/div[1]/dl/dd[1]/p/span[3]/text()').get().strip()
        # 출연진
        item['actors']=','.join(response.xpath('//*[@id="content"]/div[1]/div[2]/div[1]/dl/dd[3]/p/a/text()').getall()).strip()
        # 총 누적관객 수
        attendance=response.xpath('//*[@id="content"]/div[1]/div[2]/div[1]/dl/dd[5]/div/p[2]/text()').get()

        item['attendance']=attendance.strip() if attendance else '누적관객 0명'
        '''
        [yield 주석시]
            2021-07-23 14:08:24 [scrapy.core.engine] DEBUG: Crawled (200) <GET https://movie.naver.com/movie/bi/mi/b
            asic.naver?code=168074>
        [yield item시]
            2021-07-23 14:10:40 [scrapy.core.scraper] DEBUG: Scraped from <200 https://movie.naver.com/movie/bi/mi/b
            asic.naver?code=35187>
            {'director': '로만 폴란스키',
             'genre': '드라마,전쟁',
             'movieTitle': '피아니스트',
             'netizenScore': '네티즌 평점 93.3점',
             'rank': '02',
             'rankingMenu': '평점순(현재상영영화)',
             'visitorScore': '관람객 평점 9.51점'}
        '''
        yield item#Item Object반환환










