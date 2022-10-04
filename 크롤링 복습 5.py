#!/usr/bin/env python
# coding: utf-8

# ### 유투브 댓글 수집

# In[1]:


from selenium import webdriver as wb
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time


# In[11]:


# 1 크롬 키기> 유튜브로 
driver = wb.Chrome()
driver.get("https://www.youtube.com/watch?v=fRaCGfuAJX4")


# In[15]:


# 2 댓글정보 수집
review = driver.find_elements(By.ID,"content-text")
for i in review :
    print(i.text)


# In[24]:


#  수집한 댓글의 길이 체크
len(review)


# ### 스크롤 내리는 방법
#    - 키보드의 END키를 활용! 
#    - 전체 페이지를 움직이기 때문에 body 태그를 접근
#    - body 태그에게 키보드의 END값을 전달  > body.send_keys(Keys.END)
#    - 주의점) 반복 작업시 while문은 사용금지 > body태그는 계속 존재 > 무한루프
#    - for 문을 활용해서 많은 양의 반복을 통해 진행 추천! 

# In[25]:


for i in range(100) :
    body = driver.find_element(By.TAG_NAME,"body")
    body.send_keys(Keys.END)
    time.sleep(0.5)


# ### 이미지 수집 

# In[41]:


from selenium import webdriver as wb
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
# 파일 시스템을 위한 라이브러리(파일, 폴더를 생성, 삭제)
import os 
# 이미지의 url값을 파일로 변형시켜주는 라이브러리
from urllib.request import urlretrieve


# In[42]:


# 1. 크롬을 열고 네이버에 들어가기
driver = wb.Chrome()
driver.get("http://www.naver.com")


# In[44]:


# 2. 원하는 키워드 입력하고 검색하기
# 2.1 검색바를 찾기
search = driver.find_element(By.ID,"query")
#2.2 검색어 입력하기
search.send_keys('르세라핌')
#2.3 검색 누르기
search.send_keys(Keys.ENTER)


# In[49]:


# 3. 이미지탭 클릭하기
tap = driver.find_element(By.CSS_SELECTOR,"#lnb > div.lnb_group > div > ul > li:nth-child(3) > a")
tap.click()


# In[53]:


# 4. 이미지 태그들을 수집(이미지 태그 속에 존재하는 src만 추출하기 위해서)
img = driver.find_elements(By.CSS_SELECTOR,"._image._listImage")


# In[54]:


# 나 img리스트의 0번째 데이터에서 src 속성을 가져다줘! 
# 속성을 가져오는 함수 : get_attribute("속성")
img[0].get_attribute('src')


# In[55]:


# src를 담아줄 리스트 새로 제작
srcList = []
for i in img :
    srcList.append(i.get_attribute("src"))


# In[56]:


srcList


# In[57]:


# 이미지를 저장! 
# 바탕화면 이미지 폴더를 생성
# 바탕화면에 이미지라는 폴더가 없다면, 바탕화면에 이미지 폴더 만들어줘
if not os.path.isdir("C:/Users/smhrd/Desktop/이미지"):
    os.makedirs("C:/Users/smhrd/Desktop/이미지")


# In[60]:


#url 값을 이미지 폴더에 저장
cnt = 0
for i in srcList :
    urlretrieve(i,"C:/Users/smhrd/Desktop/이미지/"+str(cnt)+".jpg")
    cnt+=1


# #### 이미지가 중간에 깨지는 이유는?
# - 이미지는 텍스트 파일보다 크기가 더 크기 때문에
# - 화면상에 스크롤을 통해서 더 많이 로딩을 받기!
# - 1. 크롬 실행
# - 2. 스크롤을 충분히 진행 //화면구성
# - 3. img태그를 수집 // 태그 수집
# - 4. img태그 속 src만 추출 // 데이터 가공
# - 5. 파일로 저장 // 데이터 활용

# ## 카카오맵 데이터 수집

# In[38]:


from selenium import webdriver as wb
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
driver = wb.Chrome()
driver.get("https://map.kakao.com/")


# In[29]:


#1. 검색창에 광주 맛집 검색 
# 지도 설정 레이어를 클릭! 
layer = driver.find_element(By.ID,"dimmedLayer")
layer.click()


# ### id나 클래스에(선택자에) .,# 기호가 들어가 있는 경우
# - 컴퓨터가 해석할 때, #(아이디), .(클래스)로 인식하기 때문에
# - 문자로 인식시키기 위해서 \# or \. 사용!
# - 문자로 ".","#"으로 인식한다 

# In[39]:


#검색창 찾기
search = driver.find_element(By.CSS_SELECTOR,"#search\.keyword\.query")


# In[40]:


search.send_keys("광주맛집")
search.send_keys(Keys.ENTER)


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




