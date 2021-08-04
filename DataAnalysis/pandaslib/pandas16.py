import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
from matplotlib import  rc
#사용가능한 시스템 한글 폰트 확인
fonts = fm.findSystemFonts() #list
print(fonts)

fontsIndex = 0
for index,value in enumerate(fonts):
    if value == '/System/Library/Fonts/Supplemental/AppleGothic.ttf':
        fontsIndex = index


#사용할 한글 폰트 설정
font_name = fm.FontProperties(fname=fonts[fontsIndex])
print(font_name.get_name())

#rc로 설정하면 모든 plot에 같은 폰트가 적용됨
rc('font',family=font_name.get_name())


#표준정규분포를 따르는 shape가 (365,2)인 배열로 데이터프레임 생성
df = pd.DataFrame(np.random.randn(365,2),index=pd.date_range('2021/1/1',periods=365),columns=['코스피 지수','코스닥 지수']).cumsum()
print(df.head())
'''
df.plot()
plt.title('2021년도 일별 코스피/코스닥 지수')
plt.xlabel('일')
plt.ylabel('지수')
plt.show()
#위 그래프를 닫아야지 아래 코드가 실행된다.
'''

df2 = pd.DataFrame(np.random.rand(10,4),columns=['a','b','c','d'])
print(df2)
#df2.plot(kind='bar') #막대그래프
#df2.plot(kind='hist') #히스토그램
df2.plot(kind='bar',stacked=True,figsize=(10,5)) #누적 막대그래프 size는 inches
#df2.plot.bar() #kind에 문자열로 지정한 그래프 종류가 모두 함수형태로 제공된다.
plt.show()
