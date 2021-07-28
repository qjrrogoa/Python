import schedule
from scrapy.utils.project import get_project_settings
from scrapy.crawler import CrawlerProcess
import time
#https://schedule.readthedocs.io/en/stable/
hour,minute = input('시와 분을 입력하세요(공백)').split()

def job():
    
    #현재 파일을 scarpy.cfg와 같은 위치에 넣어야 한다
    #그래야 scrapy.cfg정보를 가져와 봇을  crawl하는 아래 API가 작동한다
    settings=get_project_settings()#<class 'scrapy.settings.Settings'>
    process=CrawlerProcess(settings)

    for spider_name in process.spiders.list():
        print('%s 스파이더가 크롤링 시작합니다...'.format(spider_name))
        process.crawl(spider_name)#scrapy crawl starbucks명령어와 같다
        process.start()#크롤링 시작



#스케줄 작성
#매일 hour시 ,minute분에 starbucts봇 실행
schedule.every().day.at('{}:{}'.format(hour,minute)).do(job)

while True:
    schedule.run_pending()
    time.sleep(1)
