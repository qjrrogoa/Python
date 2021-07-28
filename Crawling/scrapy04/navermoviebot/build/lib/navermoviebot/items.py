# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy

#스크래핑한 네이버 영화 데이타(한편의 영화정보)를 담을 자료구조 정의
class NavermoviebotItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # 영화랭킹 메뉴의  첫 페이지의 정보를 담을 변수(영화랭킹메뉴,순위,영화명)
    rankingMenu = scrapy.Field()
    rank = scrapy.Field()
    movieTitle = scrapy.Field()
    # 첫 페이지의 영화제목 클릭시 나타나는 페이지의 정보를 담을 변수(영화 상세)
    visitorScore=scrapy.Field()
    netizenScore=scrapy.Field()
    genre =scrapy.Field()
    nationality=scrapy.Field()
    showtimes=scrapy.Field()
    director = scrapy.Field()
    actors=scrapy.Field()
    attendance=scrapy.Field()



    pass
