import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
from matplotlib import rc

#한글 폰트 처리용
font = fm.FontProperties(fname='/System/Library/Fonts/Supplemental/AppleGothic.ttf',size=25).get_name()
rc('font',family=font)

#여러 라인플롯 그리기
x=range(0,50)
#그래프 제목 표시

plt.title('하나의 Axes에 여러개의 라인 플룻 그리기')
y1 = [i*2 for i in x]
y2 = [i*3 for i in x]

#방법1 : 하나의 plot함수 사용 : x데이터,y데이터, 스타일 이거를 계속 반복, 이때는 x데이터와 스타일 생략 불가
#plt.plot(x,y1,'r:',x,y2,'b-.',x,x,'gD-')

#방법2 : 여러개의 plot함수 사용: 각 라인별 style을 추가 조정 가능
plt.plot(x,y1,color='r',linestyle=':',linewidth=5,label="첫번째 라인") #label에 지정한 값은 범례에 표시된다.
plt.plot(x,y2,color='b',linestyle='-',label="두번째 라인")
plt.plot(x,x,color='g',linestyle='-.',marker='D',linewidth=3,label="세번째 라인")

plt.legend(loc=10) #loc인자로 범례의 위치 조절 : 문자열 혹은 숫자
#X,Y축에 레이블 표시
plt.xlabel('X축 데이터')
plt.ylabel('Y축 데이터')

plt.show()