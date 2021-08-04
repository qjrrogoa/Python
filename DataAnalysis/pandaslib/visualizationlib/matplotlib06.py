import numpy as np
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
from matplotlib import rc

#한글 폰트 처리용
font = fm.FontProperties(fname='/System/Library/Fonts/Supplemental/AppleGothic.ttf',size=25).get_name()
rc('font',family=font)

plt.title('각 커리큘럼의 비율')
curriculum = ['자바','파이썬','안드로이드','스프링','데이터베이스']
ratio=[35,15,20,15,15]
colors=['red','green','blue','yellow','#f7a890']
explode=[0.3,0.2,0.2,0.0,0.1]

plt.pie(x=ratio,labels=curriculum,colors=colors,shadow=True,startangle=90,autopct='%d%%')
plt.show()