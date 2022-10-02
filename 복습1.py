#!/usr/bin/env python
# coding: utf-8

# 크롤링 : 인터넷 사이트의 페이지를 수집해서 부뉼하는것, 스크래핑 기술의 일종
# 
# 스크래핑 : http를 통해 내용을 긁어서 원하는 형태로 가공
# - request : 웹페이지를 가져오는 라이브러리, 브라우저 역할을 대신(요청,응답정보를 처리)
# -  bs4 : 웹페이지를 분석하는 라이브러리(컴퓨터가 알아먹을수있는 언어로 바꾸기/html로 변형)

# In[56]:


import requests as req
from bs4 import BeautifulSoup as bs


# In[4]:


res = req.get("http://naver.com")


# In[5]:


# 200 : 성공
# 404 : 페이지 없음
# 500 : 서버오류
# 302 : 페이지 이름
print(res.status_code)


# In[6]:


res.text


# In[9]:


soup = bs(res.text,'lxml')
# 응답받은 텍스트 데이터를 html 로 변형


# 필요한 데이터 추출하기
# - soup.find("태그") : 원하는 부분을 지정
# - 변수.get_text()함수로 추출한 부분을 가져옴

# In[25]:


data = soup.select("a.nav") #리스트형태
data[0].text


# In[26]:


for i in data:
    print(i.text)


# In[103]:


res = req.get("https://search.naver.com/search.naver?where=news&sm=tab_jum&query=%EB%89%B4%EC%A7%84%EC%8A%A4")
res


# In[104]:


soup = bs(res.text,'lxml')


# In[105]:


data =soup.select("a.news_tit")
for i in data :
    print(i.text)


# ### 네이버 검색 페이지 가져오기

# In[98]:


res =req.get("https://search.naver.com/search.naver?sm=tab_hty.top&where=nexearch&query=%EC%BF%A0%ED%82%A4%EB%9F%B0%ED%82%B9%EB%8D%A4&oquery=%EC%BF%A0%ED%82%A4%EB%9F%B0&tqi=hzEQjdprvTossd0Vd0CssssstOG-389920")


# In[99]:


soup =bs(res.text,'lxml')


# In[100]:


data = soup.select('div > strong > a')
for i in data : 
    print(i.text)


# In[101]:


import pandas as pd


# In[102]:


df = pd.DataFrame(data,columns=['쿠키이름'])
df


# ### 날씨 온도 가져오기

# In[75]:


res = req.get("https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=1&ie=utf8&query=%EB%82%A0%EC%94%A8")


# In[78]:


soup = bs(res.text,'lxml')


# In[91]:


data = soup.select(" div.weather_info > div > div._today > div.weather_graphic > div.temperature_text > strong")
for i in data:
    print(i.text)


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




