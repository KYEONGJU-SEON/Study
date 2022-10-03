#!/usr/bin/env python
# coding: utf-8

# In[67]:


import requests as req
from bs4 import BeautifulSoup as bs


# In[36]:


req.get("https://www.melon.com/chart/index.htm")
# 406 = 통신 실패 ( 요청에서 처리 - 클라이언트)


# In[37]:


# 브라우저인척 하는 작업이 필요
h={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36'}
res =req.get("https://www.melon.com/chart/index.htm",headers=h)


# In[38]:


soup = bs(res.text,'lxml')


# In[39]:


# 노래제목 수집
title = soup.select("div.ellipsis.rank01>span>a")
for i in title :
    print(i.text)


# In[40]:


#가수가 여러명인 경우 가수 전체를 포함한 태그를 가져오기 
singer = soup.select("span.checkEllipsis")
for i in singer :
    print(i.text)


# In[41]:


#앨범명
album =soup.select("div.ellipsis.rank03>a")
for i in album:
    print(i.text)


# In[42]:


len(singer)


# In[43]:


titleList=[]
singers=[]
albums=[]

length = soup.select("div.ellipsis.rank01>span>a")

title = soup.select("div.ellipsis.rank01>span>a")
singer = soup.select("span.checkEllipsis")
album =soup.select("div.ellipsis.rank03>a")

for i in range(len(length)):
    titleList.append(title[i].text)
    singers.append(singer[i].text)
    albums.append(album[i].text)


# In[44]:


# 같은 데이터끼리 : list, 다른데이터 : dictionary
melon_info = {'제목':titleList,'가수':singers,'앨범명':albums}


# In[45]:


import pandas as pd


# In[48]:


melon = pd.DataFrame(melon_info)
melon.to_csv('melon.csv',encoding='utf-8')


# ### 위키문헌 윤동주 작품 리스트 가져오기

# In[50]:


res = req.get("https://ko.wikisource.org/wiki/%EC%A0%80%EC%9E%90:%EC%9C%A4%EB%8F%99%EC%A3%BC")


# In[52]:


soup = bs(res.text,'lxml')


# In[66]:


# > : 자식태그 
# 공백(띄어쓰기) : 자손태그
title = soup.select("#mw-content-text > div.mw-parser-output > ul > li a")
title[0].text


# In[65]:


print(len(title))


# In[63]:


for i in title :
    print(i.text)


# ### 영화 리뷰 수집

# In[ ]:


# 1. req 통해 리뷰 사이트 요청(응답코드200)
# 2. 컴퓨터가 이해할 수 있는 언어로 변경(bs)
# 3. soup 데이터에서 select 를 통해 리뷰 정보만 수집  


# In[82]:


res = req.get("https://movie.naver.com/movie/bi/mi/basic.naver?code=211161")


# In[83]:


soup =bs(res.text,'lxml')


# In[85]:


soup.select("div.score_reple > p > span")


# In[ ]:


# iframe : 창을 통해서 다른 서버에 있는 정보를 보여줄 때 사용한다 
# 1) F12 개발자 도구에서 atrl+f iframe 검색
# 2) 실제 사용되는  iframe 찾기 ( 화면이 파란색으로 변경)
# 3) 실제 주소로 찾아가기! ( src = "url") - 경로만 있는 경우에는 http://서버주소 까지 입력


# In[87]:


res =req.get("http://movie.naver.com/movie/bi/mi/pointWriteFormList.naver?code=211161&type=after&isActualPointWriteExecute=false&isMileageSubscriptionAlready=false&isMileageSubscriptionReject=false")


# In[89]:


soup = bs(res.text,'lxml')


# In[100]:


#불필요한 개행을 지우는 방법
review = soup.select("div.score_reple>p>span")
for i in review :
    print(i.text.strip())


# In[99]:


ico = soup.select("span.ico_viewer")
for i in ico :
    i.extract()


# In[101]:


len(review)


# ### 페이지 이동하면서 저장하기

# In[105]:


for i in tq(range(1,100)):
    res =req.get("http://movie.naver.com/movie/bi/mi/pointWriteFormList.naver?code=211161&type=after&isActualPointWriteExecute=false&isMileageSubscriptionAlready=false&isMileageSubscriptionReject=false&page="+str(i))
    soup = bs(res.text,'lxml')
    ico = soup.select("span.ico_viewer")
    for i in ico :
        i.extract()
        review = soup.select("div.score_reple>p>span")
    for i in review :
        print(i.text.strip())


# In[104]:


# 반복문 진행사항을 체크할 수 있는 라이브러리(로딩바)
from tqdm import tqdm_notebook as tq

