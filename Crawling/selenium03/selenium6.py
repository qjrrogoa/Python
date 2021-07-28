#네이버 자동으로 로그인하기
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os

# 1.WebDriver객체 얻기(자동으로 크롬브라우저 실행)
driver = webdriver.Chrome('{}{}chromedriver.exe'.format(os.path.dirname(os.path.realpath(__file__)), os.path.sep))
driver.get('https://nid.naver.com/nidlogin.login')
#아래처럼 로그인시 리캡차->이미지 텍스트인식 화면 표시됨
'''
username = WebDriverWait(driver,2).until(EC.presence_of_element_located((By.ID,'id')))
password = WebDriverWait(driver,2).until(EC.presence_of_element_located((By.ID,'pw')))
username.send_keys('아이디')
password.send_keys('비번')
password.send_keys(Keys.ENTER)
'''
#요소가 로드될때까지 기다리기
WebDriverWait(driver,2).until(EC.presence_of_element_located((By.ID,'id')))
#자바스크립트로 로그인 처리
driver.execute_script("document.getElementById('id').value='아이디';")
driver.execute_script("document.getElementById('pw').value='비번';")
driver.find_element_by_xpath('//*[@id="log.login"]').click()
#등록안함버튼 클릭처리하기
WebDriverWait(driver,2).until(EC.presence_of_element_located((By.ID,'new.dontsave'))).send_keys(Keys.ENTER)



