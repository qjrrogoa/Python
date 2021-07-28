#트위터에 로그인(1단계)후 Profile아이콘 클릭(2단계)후 Followers 클릭(3단계)후 나의  팔로워 가져오기(스크래핑)를
#자동화 하자(selenium + BeautifulSoup)
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
from bs4 import BeautifulSoup


#1.WebDriver객체 얻기
driver = webdriver.Chrome('{}{}chromedriver.exe'.format(os.path.dirname(os.path.realpath(__file__)),os.path.sep))
#2.브라우저에 트위트 로그인페이지 로딩하기
driver.get('https://twitter.com/login')
try:#명시적 대기(Explicit Wait):권장
    #1단계 로그인 하기
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
    #2단계 Profile링크 클릭처리하기
    #기대조건 설정 및 기대조건 만족할때까지 대기하기
    profile = WebDriverWait(driver,3).until(EC.presence_of_element_located((By.XPATH,'//*[@id="react-root"]/div/div/div[2]/header/div/div/div/div[1]/div[2]/nav/a[7]')))
    #방법1-WebElement객체.click()함수로 클릭
    #profile.click()
    #방법2- Profile을 클릭하지않고 a태그 요소의 링크 주소를  Webdriver의 get()의 인자로 준다
    href=profile.get_attribute('href') #href 속성을 가져오기 /아이디
    print('href속성:',href)
    # WebDriver의 get()메소드로 다시 페이지를 불러오자
    driver.get(href)#https://twitter.com/hwanyhee
    #3단계-Flowers링크 클릭처리
    followers = WebDriverWait(driver,3).until(EC.presence_of_element_located((By.CSS_SELECTOR,'#react-root > div > div > div.css-1dbjc4n.r-18u37iz.r-13qz1uu.r-417010 > main > div > div > div > div > div > div:nth-child(2) > div > div > div:nth-child(1) > div.css-1dbjc4n.r-1ifxtd0.r-ymttw5.r-ttdzmv > div.css-1dbjc4n.r-13awgt0.r-18u37iz.r-1w6e6rj > div:nth-child(2) > a')))
    followers.click()
    #클릭후 즉 페이지 이동후 현재 드라이버의 url
    print(driver.current_url)#https://twitter.com/hwanyhee/followers

    print('[나를 팔로우하는 사람들:selenium]')
    #until는 무조건 첫번째 WebElement요소 반환
    #그래서 기대조건 충족할때까지 기다리면 모든 요소가 로드되었다는 의미임으로
    WebDriverWait(driver,3).until(EC.presence_of_element_located((By.XPATH,'//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[2]/section/div/div/div/div/div/div/div[2]/div/div[1]/a/div/div[1]/div[1]/span/span')))
    #find계열로 요소 찾기
    elements=driver.find_elements(By.XPATH,'//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[2]/section/div/div/div/div/div/div/div[2]/div/div[1]/a/div/div[1]/div[1]/span/span')
    print(elements)
    for element in elements:
        print(element.text)
    print('[나를 팔로우하는 사람들:Beautifulsoup]')
    # HTML소스로 BeautifulSoup객체 생성
    soup = BeautifulSoup(driver.page_source,'html.parser')
    # BeautifulSoup객체로 스크래핑하기
    elements=soup.select('#react-root > div > div > div.css-1dbjc4n.r-18u37iz.r-13qz1uu.r-417010 > main > div > div > div > div > div > div:nth-child(2) > section > div > div > div > div > div > div > div.css-1dbjc4n.r-1iusvr4.r-16y2uox > div > div.css-1dbjc4n.r-1wbh5a2.r-dnmrzs > a > div > div.css-1dbjc4n.r-1awozwy.r-18u37iz.r-dnmrzs > div.css-901oao.css-bfa6kz.r-18jsvk2.r-1qd0xha.r-a023e6.r-b88u0q.r-rjixqe.r-bcqeeo.r-1udh08x.r-3s2u2q.r-qvutc0 > span > span')
    for element in elements:
        print(element.text)
except TimeoutException as e:
    print('해당 요소가 존재하지 않거나,해당 요소가 3초동안 로드가 되지 않았어요:',e)
finally:
    time.sleep(2)#너무 빨리 닫혀서 확인차
    driver.quit()





