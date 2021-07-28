'''
1.스타벅스 봇을 schedule 라이브러리로 스케줄링
2.1번의 스케줄링한 파이썬 프로그램이 실행되도록 배치 파일(.bat)만들기
3.2번의 배치파일을 윈도우는 작업스케줄러(리눅스는 crone)를 사용하여 등록
'''
import scrapy
#아이템 클래스 import
from starbucksbot.items import StarbucksbotItem
#셀레니움
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
#BeautifulSoup
from bs4 import BeautifulSoup

import os

class StarbucksSpider(scrapy.Spider):
    name='starbucks'
    start_urls=['https://www.starbucks.co.kr/store/store_map.do']

    def __init__(self):#브라우저 제어를 위한 WebDriver객체 생성
        # Headless Browser를 위한 옵션 설정
        options = webdriver.ChromeOptions()
        options.add_argument('headless')
        options.add_argument('window-size=1920x1080')
        options.add_argument('user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.164 Safari/537.36')

        self.driver = webdriver.Chrome('{}{}chromedriver.exe'.format(os.path.dirname(os.path.realpath(__file__)), os.path.sep),options=options)

    def parse(self, response, **kwargs):#오버라이딩
        try:
            self.driver.get('https://www.starbucks.co.kr/store/store_map.do')

            local = WebDriverWait(self.driver,timeout=5).until(EC.presence_of_element_located((By.CSS_SELECTOR,'#container > div > form > fieldset > div > section > article.find_store_cont > article > header.loca_search > h3 > a')))

            try:
                local.click()
            except:
                local.send_keys(Keys.ENTER)
            # 4.서울 찾고 클릭처리하기
            seoul = WebDriverWait(self.driver, timeout=5).until(EC.presence_of_element_located((By.XPATH,
                                                                                           '//*[@id="container"]/div/form/fieldset/div/section/article[1]/article/article[2]/div[1]/div[2]/ul/li[1]/a')))
            seoul.click()
            # 5.전체 버튼 찾고 클릭처리하기
            all = WebDriverWait(self.driver, timeout=5).until(
                EC.presence_of_element_located((By.XPATH, '//*[@id="mCSB_2_container"]/ul/li[1]/a')))
            all.click()
            # until()함수는 무조건 첫번째 거 반환:WebElement
            WebDriverWait(self.driver, timeout=5).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, '#mCSB_3_container > ul > li')))

            htmlSource = self.driver.page_source
            soup = BeautifulSoup(htmlSource, 'html.parser')
            stores = soup.select('#mCSB_3_container > ul > li')
            print(stores)
            print('서울의 스타벅스 총 매장 수:', len(stores), sep='')
            for store in stores:
                item = StarbucksbotItem()

                item['shopName'] = store.strong.text.strip()
                item['address']=store.p.text.strip()[:-9]
                item['contact'] = store.p.text.strip()[-9:]
                yield item


        except TimeoutException as e:
            self.log('찾는 요소가 없어요:',e)

