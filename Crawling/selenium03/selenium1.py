#Selenium으로 브라우저 제어 테스트 하기
from selenium import webdriver
import time
#1.웹드라이버 객체 생성
driver=webdriver.Chrome('chromedriver.exe')
print(driver ,type(driver),sep=' | ')#<class 'selenium.webdriver.chrome.webdriver.WebDriver'>
#2.사이트 요청 즉 브라우저로 사이트 로딩
driver.get(url='https://www.naver.com')
print('[WebDriver객체의 page_source속성]')
#print(driver.page_source)#html 소스
print('[WebDriver객체의 current_url속성]')
print(driver.current_url)
#3. 요소(태그) 찾기:WebDriver의 find_element계열 메소드의 반환타입은 WebElement,

driver.implicitly_wait(2)#요소를 찾을때까지 최대 지정한 초만큼 지연. 찾으면 바로 실행
#time.sleep(2)#요소를 찾든 못찾든 무조간 2초 지연
print('[2초 지연후 요소 찾기]')
#  find_elements계열은 [WebElement,....]
element=driver.find_element_by_css_selector('#themecast > div.theme_cont > div:nth-child(2) > div > ul > li > a.theme_info > strong')
print(element)

#get_attribute()는 static 속성값을 가져올때
#get_property()는 computed 속성값을 가져올때
#예 : <input type="checkebox" name="chk" checked/>
#     <input type="text" name="username"/>
#static 속성 : type or name,computed 속성:checked or value
print('[WebElement의 get_attribute("속성명")메소드]')
print('CSS셀렉터로 찾는 태그명 : ',element.tag_name)
print('[class 속성 찾기]')
#속성이 없으면 None반환
print(element.tag_name,'태그의 class속성:',element.get_attribute('class'))

print('[WebElement의 text속성]')
print(element.text)
#찾은 요소 클릭하기
element.click()
#브라우저 닫기
driver.quit()



