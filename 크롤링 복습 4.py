#!/usr/bin/env python
# coding: utf-8

# ## Selenium 모델
# - 웹페이지 제어하기 위한 모듈
# - !pip install selenium

# In[1]:


get_ipython().system('pip install selenium')


# ## Selenium  모델
# - 웹 브라우저를 자동으로 제어하기 위한 라이브러리
# - 브라우저 띄우는 것부터 제어 -> requests 가 필요없음
# - webdriver : 브라우저 역할(requests와 비슷)
# - keys : 컴퓨터에서 키보드 역할
# - By : 선택자를 선택하는 역할

# In[45]:


from selenium import webdriver as wb
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import pandas as pd
from bs4 import BeautifulSoup as bs


# In[10]:


#1 크롬창 열기(크롬드라이버설치0744)
# wb.Chrome("크롬드라이버경로/chromedriver.exe")
# 같은경로에 있을 경우 생략이 가능하다 
driver = wb.Chrome()


# In[11]:


driver.get("http://www.naver.com")


# In[19]:


search = driver.find_element(By.ID,'query')


# In[20]:


# send_keys("전달값") - 값을 전달하는 명령
search.send_keys('광주날씨')


# In[21]:


# Enter키 입력
search.send_keys(Keys.ENTER)


# In[17]:


#페이지 뒤로가기 
driver.back()


# In[26]:


#화면이 바귀면 요소를 매번 새로 탐색해야한다
search = driver.find_element(By.ID,'query')
search.send_keys("서울날씨")
btn = driver.find_element(By.ID,'search_btn')
btn.click()


# In[27]:


#창을 종료
driver.close()


# ### find_element()
# - By.ID : 아이디 선택자 이름
# - By.CLASS_NAME : 클래스 선택자 이름
# - By.CSS_SELECTOR : CSS선택자 이름
# - By.TAG_NAME : 태그를 이용해서 선택

# In[30]:


# 코로나는 언제 끝나요 입력하고 뒤로가고 창닫기
driver = wb.Chrome()
driver.get("http://www.naver.com")
search= driver.find_element(By.ID,'query')
search.send_keys("코로나는 언제 끝나요")
search.send_keys(Keys.ENTER)
driver.back()
driver.close()


# In[41]:


# 구글링에서 크롤링을 검색하여 결과 페이지를 띄우기
#1. 크롬창 띄우기
driver = wb.Chrome()
#2. 구글 접속
driver.get("https://www.google.com")


# In[42]:


search = driver.find_element(By.CLASS_NAME,'gLFyf.gsfi')


# In[43]:


search.send_keys('크롤링')
search.send_keys(Keys.ENTER)
driver.close()


# ### 웹페이지 스크롤링
# - Keys.PAGE_DOWN 활용

# In[47]:


url = 'https://www.google.com/search?q=%EB%B9%85%EB%8D%B0%EC%9D%B4%ED%84%B0&oq=%EB%B9%85%EB[…]57j0i131i433i512l2j0i512l7.1805j0j15&sourceid=chrome&ie=UTF-8'
driver=wb.Chrome()
driver.get(url)


# In[49]:


#웹페이지를 1번 스크롤링
body = driver.find_element(By.TAG_NAME,'body')
body.send_keys(Keys.PAGE_DOWN)


# In[50]:


driver.close


# In[51]:


# 3번 스크롤링 하기 
# time.sleep(1) : 1초씩 멈춤 
driver= wb.Chrome()
driver.get(url)
body = driver.find_element(By.TAG_NAME,'body')
for i in range(3):
    body.send_keys(Keys.PAGE_DOWN)
    time.sleep(1)


# ### 유투브 정보 수집
# - 영상제목/ 영상주소/조회수

# In[76]:


url_main="http://www.youtube.com/"
url_sub = "/results?search_query="
query= ' 빅데이터'


# In[77]:


driver = wb.Chrome()
driver.get(url_main+url_sub+query)
body = driver.find_element(By.TAG_NAME,'body')


# In[78]:


for i in range(5):
    body.send_keys(Keys.PAGE_DOWN)
    time.sleep(1)


# In[79]:


#driver.page_source API를 이용해 현재 렌더링 된 페이지의 Elements를 모두 가져올 수 있다.    
soup = bs(driver.page_source,'lxml')


# In[80]:


title = soup.select("h3")


# In[81]:


for i in title :
    print(i.text.strip())


# In[82]:


len(title)


# In[83]:


video_url=soup.find_all('a',id='video-title')[0]['href']


# In[84]:


url_main+video_url


# In[85]:


nums=[]
titles= []
video_urls=[]
length=soup.find_all('a',id='video-title')

for i in range(len(length)):
    title=soup.find_all('a',id='video-title')[i].text.strip()
    video_url=soup.find_all('a',id='video-title')[i]['href']
    
    titles.append(title)
    video_urls.append(video_url)
    nums.append(i+1)
    print("영상제목:" + title)
    print("영상주소:" + url_main+video_url)
    print("-"*70)


# ### 네이버 뉴스 제목, 내용 가져오기

# In[86]:


url = "https://n.news.naver.com/mnews/article/055/0000994481?sid=105"
driver = wb.Chrome()
driver.get(url)


# In[88]:


soup = bs(driver.page_source,'lxml')


# In[97]:


title = soup.select_one("h2.media_end_head_headline")


# In[99]:


print("제목 : ", title.text)

# select일때는  .text를 쓰면 오류가 난다 select_one으로 해주기! 
# 값 하나 : select_one = find
# 리스트 : select = find_all 


# In[106]:


content = soup.select_one("div.go_trans._article_content").text.strip().replace("\n","")


# In[108]:


print("내용 : ",content)


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




