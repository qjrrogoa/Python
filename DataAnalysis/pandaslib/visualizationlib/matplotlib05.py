import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import numpy as np
from matplotlib import rc

#한글 폰트 처리용
font = fm.FontProperties(fname='/System/Library/Fonts/Supplemental/AppleGothic.ttf',size=25).get_name()
rc('font',family=font)

#0부터 29까지의 난수를 100개 발생해 리스트로 변환후 x1와 y1에 저장
x1=list(np.random.randint(0,30,100))
y1=list(np.random.randint(0,30,100))

x2=list(np.random.randint(0,30,100))
y2=list(np.random.randint(0,30,100))

plt.title('산점도')
plt.xlabel('X축 데이터')
plt.ylabel('Y축 데이터')

plt.scatter(x1,y1,marker='^',c='r',label='범례1')
plt.scatter(x2,y2,marker='o',c='g',label='범례2')
#범례 표시
plt.legend()
plt.show()