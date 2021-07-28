import time
#time():1970 1.1 0시0분0초부터 현재 까지 지닌 시간을 초단위로 반환
#localtime(초):지역(한국)에 맞는  시간으로 변경 하는 함수
#https://docs.python.org/ko/3/library/time.html?highlight=strftime#time.strftime
#strftime('날짜형식의 포맷 문자열',시간)
def getYear():
    return time.strftime('%Y', time.localtime(time.time()))
def getMonth():
    return time.strftime('%m', time.localtime(time.time()))
def getDate():
    return time.strftime('%d', time.localtime(time.time()))
