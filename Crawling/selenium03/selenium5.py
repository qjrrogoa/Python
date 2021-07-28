#AJAX로 처리되는 동적인 데이타 selenium으로 가져오기
#BeautifulSoup만으로는 스크래핑 불가능
#서울의 전체 스타벅스 매장 가져오기
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os,time
from bs4 import BeautifulSoup
import json,csv

'''
Headless Browser:
화면이 존재하지 않는 브라우저로 웹 브라우저와 유사한 환경을
가졌지만 커맨드 라인 인터페이스(CLI)를 통해 실행하고 제어 할 수 있는 브라우저를
뜻한다
주로 웹 어플리케이션의 성능 테스트나 스크린 샷등에 사용한다
크롬은 윈도우 기준 크롬 59, 맥/리눅스 기준 크롬 60버전부터 크롬에 
Headless Mode가 정식으로 추가되었다.
PhantomJS역시 Headless Browser지만 크롬이 Headless를 지원하기 시작하면서
2018년부터 개발이 중단되었다
그리고 PhantomJS는 성능상의 문제점과 크롬과 완전히 동일하게 동작하지는 
않는다는 문제점이 있다. 
'''

try:
    # Headless Browser를 위한 옵션 설정
    options = webdriver.ChromeOptions()
    options.add_argument('headless')
    options.add_argument('window-size=1920x1080')
    options.add_argument('user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.164 Safari/537.36')

    # 1.WebDriver객체 얻기(자동으로 크롬브라우저 실행)
    driver = webdriver.Chrome('{}{}chromedriver.exe'.format(os.path.dirname(os.path.realpath(__file__)), os.path.sep),options=options)
    # 2.WebDriver객체의 get메소드로 특정 사이트를 브라우저에 로딩
    driver.get('https://www.starbucks.co.kr/store/store_map.do')
    '''
    #Implicit Wait 사용
    driver.implicitly_wait(5)
    # 3.지역버튼 찾고 클릭처리하기
    local=driver.find_element_by_css_selector('#container > div > form > fieldset > div > section > article.find_store_cont > article > header.loca_search > h3 > a')
    local.click()
    # 4.서울 찾고 클릭처리하기
    seoul=driver.find_element_by_xpath('//*[@id="container"]/div/form/fieldset/div/section/article[1]/article/article[2]/div[1]/div[2]/ul/li[1]/a')
    seoul.click()
    # 5.전체 버튼 찾고 클릭처리하기
    all=driver.find_element_by_xpath('//*[@id="mCSB_2_container"]/ul/li[1]/a')
    all.click()
    #웹드라이버로 요소(li:각 지점데이타를 감싸는 태그)를 찾을때까지 기다린다
    #아래 라인 주석시 stores는 []
    driver.find_element_by_css_selector('#mCSB_3_container > ul > li')

    #뷰티플스프로 스크래핑하기
    htmlSource=driver.page_source
    soup = BeautifulSoup(htmlSource,'html.parser')
    stores=soup.select('#mCSB_3_container > ul > li')
    print(stores)
    print('서울의 스타벅스 총 매장 수:',len(stores),sep='')
    for store in stores:
        print(store.text)
    '''
    #Explicity Wait사용하기:기대조건을 만족할때까지 대기
    # 3.지역버튼 찾고 클릭처리하기
    local = WebDriverWait(driver,timeout=5).until(EC.presence_of_element_located((By.CSS_SELECTOR,'#container > div > form > fieldset > div > section > article.find_store_cont > article > header.loca_search > h3 > a')))

    # click()함수 호출시
    # selenium.common.exceptions.WebDriverException: Message: unknown error: Element <a href="javascript:void(0);">...</a> is not clickable at point (169, 228). Other element would receive the click: <div class="loading_dimm" style="z-index: 20000; display: block; opacity: 0.417742;"></div>
    # 에러발생
    # click()함수 사용시 에러발생시 처리방법
    try:
        local.click()
    except:
        local.send_keys(Keys.ENTER)
    #4.서울 찾고 클릭처리하기
    seoul = WebDriverWait(driver, timeout=5).until(EC.presence_of_element_located((By.XPATH,'//*[@id="container"]/div/form/fieldset/div/section/article[1]/article/article[2]/div[1]/div[2]/ul/li[1]/a')))
    seoul.click()
    # 5.전체 버튼 찾고 클릭처리하기
    all = WebDriverWait(driver, timeout=5).until(EC.presence_of_element_located((By.XPATH,'//*[@id="mCSB_2_container"]/ul/li[1]/a')))
    all.click()
    #until()함수는 무조건 첫번째 거 반환:WebElement
    WebDriverWait(driver, timeout=5).until(EC.presence_of_element_located((By.CSS_SELECTOR,'#mCSB_3_container > ul > li')))
    '''
        서울 선택후 전체 버튼 클릭시 데이타를 ul태그사이에 li태그로 Ajax를 이용해
        동적으로 추가한다 
        < !-- 검색결과  없는   경우 -->
        < !--p  class ="no_result" > 검색 결과가 없습니다.< / p-->

        < !-- 검색결과 있는  경우 -->
        < div  class ="result_list scrollbar-inner" >
        < ul  class ="quickSearchResultBoxSidoGugun" >

        < / ul >
        < / div >
        따라서 
        li가 생길때까지 기다린다 즉 아래 CSS셀렉터 이용
        '#mCSB_3_container > ul > li'
    '''
    htmlSource = driver.page_source
    soup = BeautifulSoup(htmlSource, 'html.parser')
    stores = soup.select('#mCSB_3_container > ul > li')
    print(stores)
    print('서울의 스타벅스 총 매장 수:', len(stores), sep='')
    #.json 혹은 .csv파일로 저장하기
    list_ = []#[{'store':'역삼점','location':'가산동','contact':'010-1234'},{}.....]

    for store in stores:
        #print(store.text)
        storeName=store.strong.text.strip()
        location=store.p.text.strip()[:-9]
        contact=store.p.text.strip()[-9:]
        dict_ = {'store':storeName,'location':location,'contact':contact}
        list_.append(dict_)
    #print(list_)
    # 파이썬 객체를 JSON형태의 문자열로 변경
    objToJsonString=json.dumps(list_,indent=4,ensure_ascii=False)
    #JSON형태의 문자열을 .json파일로 저장
    with open('starebucks.json','w',encoding='utf8') as f:
        f.write(objToJsonString)

    # CSV파일로 저장하기
    with open('starebucks.csv', 'w', encoding='utf8',newline='') as f:
        header=['store','location','contact']
        writer= csv.DictWriter(f,fieldnames=header)
        writer.writeheader()
        writer.writerows(list_)

except TimeoutException as e:
    print('해당 요소가 존재하지 않거나,해당 요소가 3초동안 로드가 되지 않았어요:', e)
finally:
    time.sleep(2)  # 너무 빨리 닫혀서 확인차
