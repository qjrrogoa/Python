import numpy as np
import pandas as pd

#데이터 프레임 데이터 참조하기 1
dic = {'names':['가길동','나길동','다길동','라길동'],'score':[90,56,87,70],'grade':['A','F','B','C']}
df = pd.DataFrame(dic)
print(df)
print(df.head(2))
print(df.tail(2))
print(df.sample()) #랜덤하게 1개의 데이터를 반환 숫자 n를 지정 가능
print(df.describe())
print(df.describe(include='all'))

#열 가져오기
df2 = pd.DataFrame(dic,columns=['names','years','score','grade','major'],index=list('가나다라'))
print(df2)
print(df.info()) #결측치 존재 유무 판단하

#하나의 열 참조. 데이터프레임객체["컬럼명"] 혹은 데이터프레임객체.컬럼명
print(df2['names']) #혹은 df.names. 시리즈명은 컬럼
print(df2.score)

#두개의 열 참조
#데이터 프레임객체[['컬럼명1','컬럼명2',...]]
#데이터프레임 형태로 가져온다
#반드시 [[]] 형태
print(df[['names','score']]) #데이터 프레임

#기존 열에 값 설정하기
#df2.major = '컴퓨터공학' #일괄적으로 대입시에는 값(스칼라)만
df2.major=['컴퓨터공학','산업공학','전자공학','토목공학'] #여러개의 값 설정시 튜플이나 리스트로
print(df2)

#데이터 프레임 생성 후 열 생성 및 값 추가하기
#df2['컬럼명']형태로 컬럼 추가
#df2.addr = ['가산동','나산동','다산동','라산동'] # 에러!
df2['addr'] = ['가산동','나산동','다산동','라산동']
print(df2)

#넘파이 배열로 값 대입
df2['ages']=np.random.randint(low=20,high=30,size=4)
print(df2)

#Series로 값 대입
#기존의 행 index와 동일한 이름으로 시리즈의 index를 설정하면
#데이터프레임의 행 인덱스에 맞추서 시리즈 데이터가 설정된다
#일치하지 않은 인덱스는 NaN

column_series = pd.Series(data=['2021학번','2019학번'],index=['가','라'])
df2['hakbun']=column_series
print(df2)

#기존 열의 값을 연산해서 새로운 열의 값으로 대입
print(df2.score >= 80)
df2['pass'] = df2.score >= 80
print(df2)
