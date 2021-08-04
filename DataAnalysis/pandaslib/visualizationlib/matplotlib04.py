import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import numpy as np
from matplotlib import rc

#한글 폰트 처리용
font = fm.FontProperties(fname='/System/Library/Fonts/Supplemental/AppleGothic.ttf',size=25).get_name()
rc('font',family=font)

#막대에 데이터 수치(고도 : altitude)를 표시하려면 아래 두 줄이 필요함
fig = plt.figure(figsize=(12,8))
axes = fig.add_subplot(1,1,1) #1행 1열자리 axes.인덱스는 1

plt.title('산의 높이 비교')
#막대 레이블:
mountains=['설악선','덕유산','속리산','태백산','대둔산','비슬산','소백산','한라산','성인봉']
#막대 데이터(Y좌표)
y=[2023,2003,1895,1930,1745,1456,2030,2090,1090]
#막대가 그려질 위치값(X좌표)
x=np.arange(len(mountains))

#수직 막대 그리기
rects=plt.bar(x,y,color='g')

#X축에 산이름으로 티커표시
plt.xticks(x,mountains)

#Y레이블 표시
plt.ylabel('고도')

#막대에 데이터 수치 표시하기
for index,rect in enumerate(rects):
    #test(x좌표,y좌표,'텍스트')
    axes.text(rect.get_x()+rect.get_width()/2,0.9*rect.get_height(),str(y[index])+'미터',horizontalalignment='center',fontdict={'color':'white','size':12})
plt.show()
