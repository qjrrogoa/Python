import matplotlib.pyplot as plt
#Y좌표만으로 그래프 그리기
#y좌표만으로 이루어진 그래프(데이터는 리스트 혹은 튜플)
#plt.plot([1,2,3]) #y=[1,2,3],x=[0,1,2] 즉 (x,y)는 (0,1),(1,2),(3,2)그래프가 그려진다
#plt.plot([1,2,3],'r*-.') #y좌표하고 '스타일'설정
                        #스타일은 '색상,마커,라인스타일' 순이다.
#plt.show()


#X,Y좌표로 그래프 그리기
x=range(1,4)
y=[i * 2 for i in x]
#plt.plot(x,y,marker='o')
#plt.plot(x,y,color='g',marker='+',linestyle='-.')
plt.plot(x,y,'g+-.')#위와 같다

#x축 y축 값 설정 : plt.axis()
#[x축 시작값, x축 끝값, y축 시작값, y축 끝값] 동시에 x축의 시작값과 끝값, y축의 시작값과 끝값 ]

#plt.axis([x[0],x[len(x)-1],y[0],y[len(y)-1]])
plt.xticks(x)
plt.yticks(y)
plt.grid()
plt.show()