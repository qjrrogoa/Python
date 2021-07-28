#트위터에 자동으로 로그인하기
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
#Implicit Wait혹은 Explicit Wait든 지정한 시간동안 요소를 못찾을때 발생하는 예외
from selenium.common.exceptions import TimeoutException
#위치 지정자(셀렉터)를 위한 클래스
from selenium.webdriver.common.by import By
#WebDriverWait는 Selenium 2.4.0 이후 부터 사용 가능
#기대조건이 만족할때까지 기다리기 위한 함수 사용을 위한 클래스
from selenium.webdriver.support.ui import WebDriverWait
# expected_conditions는 Selenium 2.26.0 이후 부터 사용 가능
# 기대조건을 설정하기위한 클래스
from selenium.webdriver.support import expected_conditions as EC
import os,time

#1.WebDriver객체 얻기
driver = webdriver.Chrome('{}{}chromedriver.exe'.format(os.path.dirname(os.path.realpath(__file__)),os.path.sep))
#2.브라우저에 트위트 로그인페이지 로딩하기
driver.get('https://twitter.com/login')
try:#명시적 대기(Explicit Wait):권장
    #아이디 및 비밀번호 입력  요소 얻기
    #3.기대조건 설정
    username_ec=EC.presence_of_element_located((By.NAME,'session[username_or_email]'))
    password_ec=EC.presence_of_element_located((By.NAME,'session[password]'))
    print(type(username_ec))#<class 'selenium.webdriver.support.expected_conditions.presence_of_element_located'>
    #4.위 기대조건을 만족할때까지 Wait
    username=WebDriverWait(driver,timeout=3).until(username_ec)
    print(username)#WebElement
    password=WebDriverWait(driver,timeout=3).until(password_ec)
    #5.각 입력창에 텍스트 보내기
    username.send_keys('아이디')
    password.send_keys('비번')
    # 6.Enter키를 누르기
    password.send_keys(Keys.ENTER)


except TimeoutException as e:
    print('해당 요소가 존재하지 않거나,해당 요소가 3초동안 로드가 되지 않았어요:',e)
finally:
    time.sleep(2)#너무 빨리 닫혀서 확인차
    driver.quit()





