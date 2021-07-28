# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter

import json,csv

#필터링(원치 않는 데이타는 가져오지 않도록 필터링한다)은 실행순서가 빠른
#파이프라인에만 적용하면 된다
#만약 실행순서가 느린 파이프라인에 필터링을 적용하면
#실행순서가 빠른 파이프 라인에는 적용이 안된다
#즉 실행순서가 빠른 파이프라인에만 적용하면 모든 파이프라인에 적용된다

#특정 단어 필터링하기 위한 모듈 import
from scrapy.exceptions import DropItem


class NavermoviebotJSONPipeline:

    forbidenWords=['범죄','전쟁','공포']

    def open_spider(self, spider):
        self.file = open('naver_movie.json', 'w', encoding='utf-8')

    def close_spider(self, spider):
        self.file.close()

    def process_item(self, item, spider):
        # JSON파일에 금지어 미 적용
        #line = json.dumps(dict(item), ensure_ascii=False)
        #self.file.write(line + '\n')
        # JSON파일에 금지어 적용하기
        # 금지어가 포함된 장르는 아이템은 제외

        isExist = False
        for forbidenWord in NavermoviebotJSONPipeline.forbidenWords:
            if forbidenWord in item['genre']:
                isExist=True
                break

        if isExist:
            raise DropItem('금지어 출현 : {}'.format(forbidenWord))
        else:
            line = json.dumps(dict(item), ensure_ascii=False)
            self.file.write(line + '\n')
        return item

class NavermoviebotCSVPipeline:

    def open_spider(self, spider):

        self.file = open('naver_movie.csv', 'w', encoding='utf-8', newline='')
        self.writer = csv.DictWriter(self.file, fieldnames=['rankingMenu', 'rank', 'movieTitle','visitorScore','netizenScore','genre','nationality','showtimes','director','actors','attendance'])
        self.writer.writeheader()

    def close_spider(self, spider):
        self.file.close()

    def process_item(self, item, spider):
        self.writer.writerow(item)
        return item
