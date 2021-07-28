#크롬 브라우저 실행->구글사이트->selenium 타이핑->엔터 :selenium으로 자동화
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import os,random,time #표준 라이브러리
#__file__:현재 스크립트파일(selenium2.py)이 위치한 물리적 경로
print('현재 파일의 물리적 경로:',__file__,sep='')
#os.path.realpath():실제 운영체제에 따른 경로 표기법 반환
print('운영체제에 맞는 현재 모듈의 물리적 경로:',os.path.realpath(__file__),sep='')
#os.path.dirname():디렉토리 경로 반환
print('운영체제에 맞는 현재 모듈의 물리적 경로(디렉토리):',os.path.dirname(os.path.realpath(__file__)),sep='')
#크롬드라이버(chromedriver.exe)가 위치한 경로(절대 경로)
print('크롬드라이버의 물리적 전체 경로:','{}{}chromedriver.exe'.format(os.path.dirname(os.path.realpath(__file__)),os.path.sep))
#1.WebDriver객체 얻기
driver = webdriver.Chrome('{}{}chromedriver.exe'.format(os.path.dirname(os.path.realpath(__file__)),os.path.sep))
'''
selenium은 기본적으로 웹 자원들이 모두 로드될때까지 
기다린다
또한 implicitly_wait메소드를 통해 모든 자원이 로드될때 까지 
기다리게 하는 시간을 직접 설정할 수도 있다.
'''
#2.implicitly_wait(초)로 최대 지정한 초까지 요소가 나타날때까지 기다리기
driver.implicitly_wait(random.randint(3,5))
#3.get('사이트 주소')함수로 1번에서 실행된 크롬 브라우저에 사이트 띄우기
driver.get('https://www.google.com')#자동으로 크롬 브라우저에 구글 페이지가 보인다
#4.find_element계열(s가 붙지 않는 메소드)로 찾은 경우:WebElement객체 반환
#element=driver.find_element_by_name('q')#<input type="text" name="q" ..../>요소 찾기
#print(element)
#5.찾은 요소에 send_keys()함수로 값 보내기
#element.send_keys('selenium')#자동으로 입력상자에 selenium라는 검색어를 넣는다
#6. Enter 키 입력하기
#element.send_keys(Keys.ENTER)
#혹은
#element.send_keys(Keys.RETURN)

#4.find_elements계열로 찾은 경우:리스트 반환[WebElement,.....]
elements=driver.find_elements_by_name('q')
print(elements)
elements[0].send_keys('selenium')

#엔터키로 검색하기
#elements[0].send_keys(Keys.ENTER)

#혹은 버튼 클릭해서 검색하기
#driver.find_element_by_name('btnK').click()
#혹은 form요소 찾아서 submit()함수로 검색하기
driver.find_element_by_xpath('/html/body/div[1]/div[3]/form').submit()
#자바스크립트 자동으로 실행하기:execute_script('자스 코드')
driver.execute_script('alert("자동으로 자스 실행하기");')
#2초 지연하기
time.sleep(2)
#브라우저 닫기
driver.quit()












