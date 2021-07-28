# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter

import csv
#setting.py의 ITEM_PIPELINES부분 주석 풀기
class StarbucksbotPipeline:
    def open_spider(self, spider):
        self.file = open('starbucks.csv', 'w', encoding='utf-8', newline='')
        #fieldnames키워드인수 필수
        self.writer = csv.DictWriter(self.file,fieldnames=['shopName','address','contact'])
        #self.writer.writeheader()
    def close_spider(self, spider):
        self.file.close()

    def process_item(self, item, spider):
        self.writer.writerow(item)
        return item

