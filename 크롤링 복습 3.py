#!/usr/bin/env python
# coding: utf-8

# In[1]:


import requests as req
from bs4 import BeautifulSoup as bs
import pandas as pd


# ### 환율 가져오기

# In[33]:


url_main ="https://finance.naver.com/"
url_sub = "marketindex/exchangeList.naver"
page = url_main + url_sub
res = req.get(page)
soup = bs(res.text,'lxml')


# In[26]:


money = soup.select("td.tit>a")
for i in money:
    print(i.text)


# In[27]:


len(money)


# In[28]:


sale = soup.select("td.sale")
for i in sale:
    print(i.text)


# In[29]:


len(sale)


# In[34]:


length = soup.select("td.tit>a")

num=[]
moneys=[]
sales=[]

for i in range(len(length)):
    num_ = i+1
    money = soup.select("td.tit>a")[i].text.strip()
    sale = soup.select("td.sale")[i].text
    
    num.append(num_)
    moneys.append(money)
    sales.append(sale)
    


# In[35]:


money_info={'num' : num , '통화명' : moneys,'매매가격' :sales}
money = pd.DataFrame(money_info)
money.set_index('num',inplace=True)


# In[36]:


money.to_csv('money.csv',encoding='utf-8')
money.head(3)


# ### 페이지 이동하며 가져오기

# In[37]:


url="https://pjt3591oo.github.io/"
res=req.get(url)
soup=bs(res.content,'lxml')


# In[42]:


title = soup.select("div.p>h3>a")
len(title)


# In[53]:


author = soup.select("p.author>span")
for i in author :
    print(i.text)


# In[52]:


content =soup.select("div.p>h4")
len(content)


# In[56]:


num = 2 
while True :
    sub_url = "page"+str(num)
    page = url+sub_url
    res = req.get(page)
    soup = bs(res.text,'lxml')
    
    
    title = soup.select("div.p>h3>a")
    content =soup.select("div.p>h4")
    author = soup.select("p.author>span")
    
    for i in range(len(title)):
        print('제목 : ' +  title[i].text)
        print('내용 : ' + content[i].text)
        print('저자 : ' + author[i].text[-3:])
        
    num+=1
    
    if res.status_code!=200:
        print('종료')
        break;


# ### 종목명, 현재가격, 거래량

# In[89]:


res = req.get("https://finance.naver.com/sise/sise_quant.naver")


# In[90]:


soup =bs(res.text,'lxml')


# In[91]:


title = soup.select("a.tltle")
for i in title :
    print(i.text)


# In[92]:


price = soup.select( "td.number:nth-child(3)")
for i in price:
    print(i.text)


# In[93]:


volume=soup.select( "td.number:nth-child(6)")


# In[94]:


titles = []
prices = []
volumes = []

length = soup.select("a.tltle")

for i in range(len(length)):
    title = soup.select("a.tltle")[i].text
    price = soup.select( "td.number:nth-child(3)")[i].text
    volume=soup.select( "td.number:nth-child(6)")[i].text
    
    titles.append(title)
    prices.append(price)
    volumes.append(volume)


# In[97]:


price_info = {'종목명':titles,'거래가':prices,'거래량':volumes}
import pandas as pd
price = pd.DataFrame(price_info)
price.to_csv('price.csv',encoding='utf-8')


# In[98]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




