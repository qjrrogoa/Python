import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
from matplotlib import rc

#한글 폰트 처리용
font = fm.FontProperties(fname='/System/Library/Fonts/Supplemental/AppleGothic.ttf',size=25).get_name()
rc('font',family=font)

x=range(0,50)
y1=[i*2 for i in x]
y2=[i**2 for i in x]

'''
#하나의 Figure(윈도우)를 여러 Axes나누어 그래프 그리기
#방법1. Figure객체 생성 후 add_subplot()함수 사용
#figure객체 생성 - 그래프 그릴 화면의 크기도 지정 : 가로는 10인치 세로는 5인치로 설정
fig = plt.figure(figsize=(10,5))#figure함수는 윈도우 크기 설정이나, 혹은 여러 Axes를 생성할 때 주로 사용


ax1 = fig.add_subplot(1,2,1) #1행 2열 형태의 첫번째 그래프
print(ax1) #AxesSubplot(0.125,0.11;0.352273x0.77)
ax1.set_title("첫번째 그래프")
ax1.plot(y1,'g--',label='첫번째 범례')
ax1.set_xlabel('X축 데이터')
ax1.set_ylabel('Y축 데이터')
ax1.legend()
ax1.grid()

ax2 = fig.add_subplot(1,2,2) #1행 2열 형태의 두번째 그래프
ax2.set_title("두번째 그래프")
y2=[i**2 for i in x]
ax2.plot(x,y2,'r--',label='두번째 범례')
ax2.set_xlabel('X축 데이터')
ax2.set_ylabel('Y축 데이터')
ax2.legend(loc='upper right')
ax2.grid()

plt.show()
'''

'''
#방법2. Figure객체 미 사용 plt의 subplot()함수 사용
ax1 = plt.subplot(1,2,1)
ax1.set_title("첫번째 그래프")
ax1.plot(y1,'g--',label='첫번째 범례')
ax1.set_xlabel('X축 데이터')
ax1.set_ylabel('Y축 데이터')
ax1.legend()
ax1.grid()

ax2 = plt.subplot(1,2,2)
ax2.set_title("두번째 그래프")
ax2.plot(x,y2,'r--',label='두번째 범례')
ax2.set_xlabel('X축 데이터')
ax2.set_ylabel('Y축 데이터')
ax2.legend(loc='upper right')
ax2.grid()

plt.show()
'''

#방법3 : plt의 subplots()함수 사용
fig,axes = plt.subplots(2,2,figsize=(10,5))
#fig는 Figure객체
#axes는 2차원의 넘파이 배열이고 모든 요소는 AxesSubplot
print(axes[:,:])
axes[0,0].set_title('첫번째 그래프')
axes[0,0].plot(y1,'g--',label="첫번째 범례")
axes[0,0].set_xlabel('X축')
axes[0,0].set_ylabel('Y축')
axes[0,0].legend()

axes[1,0].set_title('두번째 그래프')
axes[1,0].plot(x,y2,'r:',label="두번째 범례")
axes[1,0].set_xlabel('X2축')
axes[1,0].set_ylabel('Y2축')
axes[1,0].legend()
plt.tight_layout() #여백을 넉넉하게 해줌
plt.show()