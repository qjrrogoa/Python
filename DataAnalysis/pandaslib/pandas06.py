import numpy as np
import pandas as pd
dic = {'names':['가길동','나길동','다길동','라길동','마길동'],'score':[90,56,87,70,88],'grade':['A','F','B','C','B']}
df = pd.DataFrame(dic,columns=['names','years','score','grade','major'],index=list('가나다라마'))
print(df)

'''
df['문자열'] : 이때 문자열은 컬럼 인덱스명
df.loc['문자열'] : 이때 문자열은 행 인덱스명
'''

#데이터 프레임 참조하기 4
print(df.loc['가']) #타입은 시리즈
print(pd.DataFrame(df.loc['가']).T) #시리즈를 데이터 프레임으로 변경

print(df.loc[['가','나','다']]) #데이터 프레임
print(df.loc['가':'다']) #데이터 프레임

#.loc[행시작:행끝,시작컬럼:끝컬럼]로 여러행 가져오기(컬럼 제한)
print(df.loc['나':'라,','names':'score'])
print(df.loc['나':'라','score']) #시리즈
print(df.loc['나':'라','score':]) #데이터프레

print(df.loc[:,'names']) #df['names']와 같다

print(df.loc[:,'names':'score']) #names~score까지
print(df.loc[:,['names','score']]) #names와 score 두개 칼럼

print(df.loc['가','names']) #스칼라
print(type(df.loc['가','names'])) #str

#.loc[불리언 시리즈]로 조건을 만족하는 특정 행 가져오기
print(df[df.score >= 80])
print(df.loc[df.score >= 80]) #위와 같다 그러나 열을 제한할 수 있다.
print(df.loc[df.score >= 80,'names':'score'])
print(df.loc[df.score >= 80,['names','score']])

print(df.loc[(df.score >= 70) & (df.score <= 80),['names','score']])

#기존 행 값 변경하기
#scroe가 80점 이상인 모든행의 years컬럼을 모두 25로 설정
print(df.loc[df['score']>=80,'years'])
df.loc[df['score']>=80,'years']=25
print(df)

#score가 80점이상인 모든행의 yeares컬럼은 30로,major컬럼은 컴퓨터 공학으로 설정
df.loc[df['score']>=80,['years','major']]=[30,'컴퓨터공학']
print(df)

#새로운 행 생성 및 값 설정하기
#df['행이름'] #행이 아니라 컬럼이 추가된다. 행 추가시에는 df.loc['행 이름']
#df.loc['바'] = np.nan #스칼라 주면 '바'행의 모든 컬럼이 해당 스칼라로 모두 설정
df.loc['바'] = ['바길동',np.nan,99,'A',np.nan] #리스트나 튜플
print(df)

#.iloc[행인덱스번호]로 하나행 가져오기 : Series 형태
#print(df[2]) #KeyError:2
dfi = df.iloc[2]
print(dfi) #시리즈 컬럼명이 행 인덱스
print(dfi.index)

#범위 인덱싱 - 끝 인덱스번호는 포함 안됨
#.iloc[시작인뎅스 : 끝 행인덱스]로 여러행 가져오기 : 데이터 프레임 형태
#print(df[0:3])
print(df.iloc[0:3]) #위와 같지만 컬럼을 제어할 수 있다.
print(df.iloc[2:])

print(df.iloc[1:5,0:3])
print(df.iloc[2:,2:])
print(df.iloc[:,3])
print(df.iloc[:,0]) #df['names']와 같다
print(df.iloc[:,0:3])#names부터 score까지
print(df.iloc[:,[0,3]])#names하고 grade

#.iloc[행인덱스,컬럼인덱스]로 값 하나 가져오기 : 스칼라
print(df.iloc[0,0])
#.iloc[불리언 넘파이 배열]로

#.iloc[불리언 배열]로 조건을 만족하는 특정행 가져오기
print(df[df.score >= 80])
print((df.score >= 80).values)
mask = (df.score >= 80).values
print(df.iloc[mask]) #iloc[불리언 시리즈]는 에러. iloc[불리언 넘파이 배열]

#80점 이상인 모든 행의 names컬럼부터 score까지
print(df.iloc[(df['score'] >= 80).values,0:3])
#print(df.iloc[df['score'] >= 80,0:3]) #100퍼센트 에러

# scroe 70점 이상 80점 이하 모든 열
print(df.iloc[(df['score'] >= 70).values & (df['score'] <= 80).values,:])

#기존 행 값 변경하기
df.iloc[(df['score'] >= 80).values,[1,4]]=[25,'컴퓨터 공학']
print(df)

#iloc 추가는 안된다, 수정만 가능하다
#df.iloc[6]=np.nan
df.loc['사']=np.nan #[o]행 추가
print(df)