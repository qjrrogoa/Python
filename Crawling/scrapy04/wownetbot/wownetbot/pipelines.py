# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter

import json,csv

#JSON파일로 저장하는 아이템 파이프 라인
class WownetbotJSONPipeline:#Item Pipeline클래스

    # 스파이더가 스크래핑을 할 준비가 되었을 때 호출되는 메소드
    # spider (Spider object) – the spider which was opened
    def open_spider(self,spider):
        self.file = open('wownet.json','w',encoding='utf-8')

    # 스크래핑이 끝났을때 호출되는 메소드
    # spider (Spider object) – the spider which was closed
    def close_spider(self,spider):
        self.file.close()

    # 스파이더로부터(parse(self, response)함수의 yield 아이템) Item을 받을때 마다 호출되는 메소드
    # dict형태의 데이타나 Item객체를 반환 해야 한다
    # item (Item object or a dict) – the item scraped
    # spider (Spider object) – the spider which scraped the item
    def process_item(self, item, spider):
        # 파이썬 코드로 JSON파일로 저장시 유니코드 한글처리는 ensure_ascii=False추가
        # 커맨드 라인으로 JSON파일 저장시는 settings.py에 FEED_EXPORT_ENCODING='utf-8'추가
        # 딕션너리 객체를 JSON문자열로 변경
        line= json.dumps(dict(item),ensure_ascii=False)
        self.file.write(line+'\n')
        return item

#CSV파일로 저장하는 아이템 파이프 라인
class WownetbotCSVPipeline:#Item Pipeline클래스

    def open_spider(self,spider):
        self.file = open('wownet.csv','w',encoding='utf-8',newline='')
        self.writer=csv.DictWriter(self.file,fieldnames=['src','title','date'])
        self.writer.writeheader()
    def close_spider(self,spider):
        self.file.close()
    def process_item(self, item, spider):
        self.writer.writerow(item)
        return item
