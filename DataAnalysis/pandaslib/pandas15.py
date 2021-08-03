import numpy as np
import pandas as pd

#범주형 데이터 다루기 - 데이터프레임의 함수 이용해서 더미변수
data=[
    ['남자',20,'A','매우못함'],
    ['여자',35,'B','잘함'],
    ['남자',45,'O','매우잘함'],
    ['남자',32,'AB','못함'],
    ['여자',12,'O','보통'],
    ['여자',24,'O','매우잘함'],
]
df = pd.DataFrame(data,columns=['Gender','Ages','Blood','Acomplish'])
print(df)

#데이터 프레임 전체 더미화
#Ages컬럼은 범주형 데이터가 아니라 수치형이라 더미화가 안 일어난다.
#컬럼인덱스가 자동으로 생성된다
#4개의 분류(class)를 가졌다면 하나의 컬럼 인덱스가 4개의 컬럼으로 생성된다.
#컬럼 인덱스명_클래스명 식으로 새롭게 컬럼인덱스가 생성된다.
#예:Gender -> Gender_A,Gender_B,Gender_AB,Gendder_O
print(pd.get_dummies(df))

#데이터 프레임 하나만 더미화
print(pd.get_dummies(df['Blood']))
#여러개 컬럼 더미화
print(pd.get_dummies(df[['Blood','Gender']]))
print(pd.get_dummies(data=df,columns=['Blood','Gender'])) #컬럼 다 나오고 Blood,Gender 컬럼들만 더미화

#범주형 데이터 다루기 - 사이킷런 사용해서 전처

#사이킷런 관련 모듈 import
from sklearn.preprocessing import OneHotEncoder,LabelEncoder

#데이터 프레임의 각 컬럼별 데이터타입이나 NaN데이터 수 정보 출력
print(df.info())
#select_dtypes : 데이터 프레임에서 dtype으로 특정 컬럼 선택
df = df.select_dtypes(include='object')

# 레이블 인코딩 : 범주를 숫자로 변경
# 1.INSTANTIATE
# encode labels with value between 0 and n_classes-1.
label_encoder = LabelEncoder()
#데이터프레임의 모든 요소 각 각에 fit_transform()함수를 적용하여
#범주형 데이터를 0~n-class -1 사이의 수치로 레이블 인코딩된 데이터프레임 생성
df2 = df.apply(label_encoder.fit_transform)
print('[범주형 데이터를 레이블 인코딩 시작]')
print(df2)
# TODO: create a OneHotEncoder object,and fit it to all of X
# 1. INSTANTIATE
onehot_encoder = OneHotEncoder()
# 2. FIT
onehot_encoder.fit(df)
# 3. Transform
onehot_label = onehot_encoder.transform(df)
print(onehot_label)

print('[범주형 데이터를 원핫 인코딩(희소행렬)]')
print(onehot_label.toarray()) #넘파이 배열 반환
'''
[[1. 0. 1. 0. 0. 0. 1. 0. 0. 0. 0.]
 [0. 1. 0. 0. 1. 0. 0. 0. 0. 0. 1.]
 [1. 0. 0. 0. 0. 1. 0. 1. 0. 0. 0.]
 [1. 0. 0. 1. 0. 0. 0. 0. 1. 0. 0.]
 [0. 1. 0. 0. 0. 1. 0. 0. 0. 1. 0.]
 [0. 1. 0. 0. 0. 1. 0. 1. 0. 0. 0.]]
 
 0~1열 : Gender
 2~5열 : Blood
 6~10열 : Acomplish
'''

#일부 컬럼에만 적용하기
gender_blood = df[['Gender','Blood']].values #넘파이 배열
print(gender_blood)
gender_blood_ = gender_blood.copy()
#2/3. FIT AND TRANSFORM
#레이블 인코딩
gender_blood_[:,0] = label_encoder.fit_transform(gender_blood[:,0]) #Gender를 레이블 인코딩
gender_blood_[:,1] = label_encoder.fit_transform(gender_blood[:,1]) #Gender를 레이블 인코딩
print(gender_blood)

#원핫인코딩
gender_blood = onehot_encoder.fit_transform(gender_blood).toarray() #넘파이 배열로 변경!!
print(gender_blood)

#범주형 데이터 다루기 - 범주형 데이터 탐색하기
print(df['Acomplish'].dtype)
#object타입을 범주형 타입인 category로 변경
df['Acomplish'] = df['Acomplish'].astype('category')
print(df['Acomplish'].dtype)

#범주를 [매우못함, 매우잘함, 못함, 보통, 잘함]에서 ['F','A','D','C','B']
print(df['Acomplish'])
df['Acomplish'].cat.categories = ['F','A','D','C','B']
print(df['Acomplish'])

#범주의 순서를 재정렬하는 동시에, 현재 갖고있지 않는 범주도 추가 가능
df['Acomplish'] = df['Acomplish'].cat.set_categories(['A+','A','B','C','D','F'])
print(df)
df.sort_values(by='Acomplish',inplace=True)
print(df)