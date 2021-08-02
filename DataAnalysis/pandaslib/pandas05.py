import numpy as np
import pandas as pd

dic = {'names':['가길동','나길동','다길동','라길동','마길동'],'score':[90,56,87,70,88],'grade':['A','F','B','C','B']}
df = pd.DataFrame(dic,columns=['names','years','score','grade','major'],index=list('가나다라마'))
print(df)

#행 가져오기 - 불리언 인덱싱
#df[df.컬럼명을 이용한 비교식]로 여러행 가져오기
print(df.score >=80) #시리즈
#df[불리언값을 가진 시리즈] 즉 True에 해당하는 행만 슬라이싱 한다
print(df[df.score>=80]) #80점 이상인 학생만 가져오기
#'합격여부' 컬럼 추가 및 점수에 따라 80점 이상이면 합격,미만이면 불합격을 컬럼의 값으로 설정
df['합격여부']=['합격' if i >= 80 else '불합격' for i in df.score ]
print(df)

#&나 | 연산자를 이용해서 여러개의 마스크를 조건으로 사용해서 어려행 가져오기
print((df['score'] >= 70) & (df['score'] <=90))

mask = (df['score'] >= 70) & (df['score'] <=90) #반드시 ()로 감싼다
print(df[mask])

#조건에 맞지 않으면 Empty DataFrame나온다.
df_score = df[df['score']>=95]
print(df_score)
print(df_score.empty)
