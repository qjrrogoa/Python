#!/usr/bin/env python
# coding: utf-8

# ### 공공데이터 포털

# In[1]:


get_ipython().run_line_magic('ls', '-al')


# In[2]:


get_ipython().run_line_magic('pwd', '')


# In[3]:


get_ipython().run_line_magic('mkdir', 'data')


# In[4]:


get_ipython().run_line_magic('ls', '')


# In[ ]:





# In[5]:


get_ipython().run_line_magic('ls', '')


# In[6]:


#라이브러리 불러오기
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
from matplotlib import rc
import seaborn as sns


# In[7]:


#한글 폰트 처리용
font = fm.FontProperties(fname='/System/Library/Fonts/Supplemental/AppleGothic.ttf',size=25).get_name()
rc('font',family=font)


# In[8]:


# minus폰트 처리용
rc('axes',unicode_minus=False)


# In[9]:


#파일 불러오기
#파일을 메모장으로 열어서 다른이름으로 저장시 인코딩을 utf-8로 선택후 저장
df = pd.read_csv('./data/도로교통공단_사망 교통사고 정보_20201231.csv',encoding='cp949')


# In[10]:


df.shape


# In[11]:


df.head()


# In[12]:


df.info()


# In[13]:


df.columns


# In[14]:


df.dtypes #각 column의 데이터 타입을 확인


# In[15]:


df.isnull().sum()


# ## 결측치 처리하기

# In[16]:


df['추가컬럼2'] = np.nan
df.insert(5,'추가컬럼1',np.nan)
nan = df.isnull().sum()


# In[17]:


df_nan = nan.reset_index() #시리즈를 데이터프레임으로 변경


# In[18]:


df_nan


# In[19]:


#컬럼 인덱스 변경하기
df_nan.columns=['컬럼명','결측치수']
df_nan


# In[20]:


df_nan.sort_values('결측치수',ascending=False)


# In[21]:


#결측치가 1000개 이상 있는 행들의 모든 컬럼들 보기
df_nan.loc[df_nan['결측치수']>1000,:]


# In[22]:


#결측치가 1000개 이상 있는 행들의 모든 컬럼들 보기
df_nan_columns = df_nan[df_nan['결측치수']>1000]#위와 같다


# In[23]:


drop_columns = df_nan_columns['컬럼명'].tolist() #시리즈를 리스트로 변환 시리즈객체.tolist()


# In[24]:


df.columns


# In[25]:


#결측치가 1000개이상인 컬럼들은 제거하자
#열을 기준으로 삭제해야하기 때문에 axis=1을 지정. 행을 삭제하려면 0(디폴트)
df.drop(drop_columns,axis=1,inplace=True)


# In[26]:


df.columns


# In[27]:


#전체 컬럼에 대한 수치 통계정보 보기
df.describe()


# In[28]:


df[['사망자수','중상자수']].describe()


# In[29]:


df.describe(include='all') 


# In[30]:


df.describe(include='object') #문자열인 컬럼만 통계


# In[31]:


#요일컬럼의 유니크한 데이터보기
df['요일'].unique()


# In[32]:


#각 요일별 교통사고 발생 빈도수
df.groupby('요일').size()


# In[33]:


#유니크한 데이터(범주형 데이터)의 총 수 반환
df['요일'].nunique() 


# In[34]:


df.사고유형_중분류.nunique()


# In[35]:


sido = df['발생지시도'].value_counts() #디폴트가 자동으로 내림차순


# In[36]:


#시도별 교통사고 발생 건수 시각화
sns.countplot(data=df,x='발생지시도',order=sido.index)


# In[37]:


df[df['발생지시도']=='서울']


# In[38]:


#서울의 요일별 교통사고 발생 빈도수
weekday = ((df[df['발생지시도']=='서울'])['요일']).value_counts()
weekday = weekday.reset_index()
weekday.columns=['요일','발생건수']
weekday


# In[39]:


#sns.barplot(x='요일',y='발생건수',data=weekday) #서울 지역만
sns.countplot(x='요일',data=df[df['발생지시도']=='서울'])


# In[40]:


#서울에서는 어느 시군구가 교통사고가 많이 발생하는가?
df.loc[df['발생지시도']=='서울']['발생지시군구'].value_counts()


# In[41]:


#and는 &, or은 |를 사용
#발생지시도가 서울이고 가해자_당사자종별가 승용차인 행만 추출
df_seoul_sedan = df[(df['발생지시도']=='서울') & (df['가해자_당사자종별']=='승용차')]


# In[42]:


df_seoul_sedan.shape #(86, 23)


# In[43]:


df_seoul_sedan.head()


# In[44]:


df_seoul_sedan['발생지시군구'].value_counts()


# In[45]:


#방법 1
#fig=plt.figure(figsize=(15,8))

fig = plt.figure(figsize=(15,8))
axes = fig.add_subplot(1,1,1) #1행 1열자리 axes.인덱스는 1
sns.countplot(x='발생지시군구',data=df_seoul_sedan,ax=axes)


# In[46]:


df_seoul_sedan_gungu = df_seoul_sedan['발생지시군구'].value_counts()


# In[47]:


#서울의 시구구명만 리스트로 변환
df_seoul_sedan_gungu.index.tolist()


# In[48]:


#서울의 시군구명만 넘파이배열로 변환
np.array(df_seoul_sedan_gungu.index)


# In[49]:


#도로형태에서 '기타'가 포함된 행은 제외
df_seoul_sedan['도로형태'].value_counts()


# In[50]:


#df_seoul_sedan[~df_seoul_sedan['도로형태'].str.contains('기타')]
df_seoul_sedan=df_seoul_sedan[df_seoul_sedan['도로형태'].str.find('기타')==-1]


# In[51]:


df_seoul = df[df['발생지시도']=='서울']


# In[52]:


df_seoul.shape #(218,23)


# In[53]:


sns.scatterplot(x='경도',y='위도',data=df_seoul,hue='사고유형_대분류')


# ## Folium

# In[55]:


import folium


# In[61]:


map = folium.Map(location=[df_seoul_sedan['위도'].mean(),df_seoul_sedan['경도'].mean()],zoom_start=12)


# In[62]:


map


# In[70]:


for row_index in df_seoul_sedan.index:
    death_count=df_seoul_sedan.loc[row_index,'사망자수']
    accident_count=df_seoul_sedan.loc[row_index,'부상자수']
    latitude = df_seoul_sedan.loc[row_index,'위도']
    longitude = df_seoul_sedan.loc[row_index,'경도']
    popuptext="<h4>사망자수 : {}</h4><h5>부상자수:{}</h5>".format(death_count,accident_count)
    location=[latitude,longitude]
    iframe = folium.IFrame(popuptext,width=300,height=150)
    popup = folium.Popup(iframe)
    folium.Marker(location=location,popup=popup).add_to(map)


# In[71]:


map


# In[72]:


map.save('index.html')


# In[ ]:




