from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os,time
from bs4 import BeautifulSoup
import requests

'''
ext: 스크래핑 이미지 확장자 .[ex] : 'png' 혹은 'jpg'
dirpath: 스크래핑한 이미지를 저장할 디렉토리 명. [ex] : 'naver' 혹은 'google'
url : 스크래핑할 url. [ex] : 'https://www.google.com/search?q={}&sxsrf=ALeKk02aqZ_Du1tRnfKxD80NOvDFxZTtzg:1610336833601&source=lnms&tbm=isch&sa=X&ved=2ahUKEwjz0L2X_JLuAhUTy4sBHXRgAK4Q_AUoAXoECBAQAw&biw=1455&bih=636'
selector : 스크래핑할 모든 이미지 요소(img)의 CSS Selector 
            [ex] 구글 이미지인 경우
            CSS Selector:
            #islrg > div.islrc > div > a.wXeWr.islib.nfEiy.mM5pbd > div.bRMDJf.islir > img


'''
def imageScrapping(ext,dirpath,url,selector,**kwargs):
    #1. 스크래핑한 이미지를 저장할 디렉토리 생성
    if not os.path.isdir(dirpath):
        os.mkdir(dirpath)
    # 2. 크롬 드라이버가 위치한 경로
    chrome_path ='{}{}chromedriver.exe'.format(os.path.dirname(os.path.realpath(__file__)),os.path.sep)
    # 3.WebDriver객체 얻기
    driver = webdriver.Chrome(chrome_path)
    try:
        # 4.url로 요청 보내기
        driver.get(url)
        #5.모든 데이타를 로딩하도록 자바스크립트로 스크롤이 안될때까지 스크롤링한다
        # 스크롤전 전체 높이 구하기
        last_scrollHeight=driver.execute_script('return document.body.scrollHeight')
        #print('last_scrollHeight:',last_scrollHeight,sep='')
        while True:#스크롤했을때의 높이 new_scrollHeight와 last_scrollHeight같을때 break
            #자바스크립트로 아래로 스크롤하기:window.scrollTo(x좌표,y좌표)
            driver.execute_script('window.scrollTo(0,document.body.scrollHeight)')
            # 컨텐츠가 로드될때까지 다음 코드 진행을 멈춘다
            time.sleep(3)
            #스크롤 후 높이 다시 구하기
            new_scrollHeight = driver.execute_script('return document.body.scrollHeight')
            if new_scrollHeight == last_scrollHeight:#같으면 더 이상 스크롤할 데이타가 없다.break
                break;
            # 높이가 같지 않으면 새로운 높이를 이전 높이로 다시 셋팅
            last_scrollHeight = new_scrollHeight


        #6.스크롤링이 끝난후 이미지 스크래핑하기
        WebDriverWait(driver,2).until(EC.presence_of_element_located((By.CSS_SELECTOR,selector)))


        #Selenium API사용
        '''
        images=driver.find_elements_by_css_selector(selector)#[WebElement,......]
        #이미지명 네이밍 방식:고양이1.jpg 고양이2.jpg.....
        #print(kwargs['query'])
        indexing=1#이미지명에 사용할 인덱스
        for image in images:
            print('image:',image)
            #img태그의 src속성 가져오기(이미지의 url)

            image_url = image.get_attribute('src')
            if image_url !=None and (image_url.find('https')==0 or image_url.find('http')==0):
                #이미지로 저장
                res=requests.get(image_url)
                with open(os.path.join(dirpath,kwargs['query']+str(indexing)+'.'+ext),'wb') as f:
                    f.write(res.content)
                indexing+=1

        '''
        #BeautifulSoup 사용

        soup = BeautifulSoup(driver.page_source,'html.parser')
        images = soup.select(selector)

        indexing = 1  # 이미지명에 사용할 인덱스
        for image in images:
            #print('image:',image)
            image_url = image.get('src') if image.get('src') else image.get('data-src')
            #print('image_url:',image_url,sep='')
            if image_url != None and (image_url.find('https') == 0 or image_url.find('http') == 0):
                # 이미지로 저장
                res = requests.get(image_url)
                with open(os.path.join(dirpath, kwargs['query'] + str(indexing) + '.' + ext), 'wb') as f:
                    f.write(res.content)
                indexing += 1

    except Exception as e:
        print('요소를 찾지 못했어요:',e)
    finally:
        time.sleep(5)
        driver.quit()
        return indexing-1
if __name__ =='__main__':
    query = input('스크래핑할 이미지 종류를 입력하세요?')
    #네이버 이미지
    '''
    url = 'https://search.naver.com/search.naver?where=image&query={}'.format(query)
    selector='#main_pack > section > div > div.photo_group._listGrid > div.photo_tile._grid > div > div > div.thumb > a > img'
    #네이버 이미지 스크래핑
    numberOfImages=imageScrapping('jpg','naver',url,selector,query=query)
    '''
    #구글 이미지
    url ='https://www.google.com/search?q={}&rlz=1C1CHBD_koKR942KR942&source=lnms&tbm=isch&sa=X&ved=2ahUKEwjw6cHn3PPxAhUNAd4KHTFlC64Q_AUoAXoECAEQAw&biw=1920&bih=925'.format(query)
    selector='#islrg > div.islrc > div > a.wXeWr.islib.nfEiy > div.bRMDJf.islir > img'
    numberOfImages = imageScrapping('jpg', 'google', url, selector, query=query)
    print('총 {}개의 이미지가 스크래핑 되었습니다'.format(numberOfImages))