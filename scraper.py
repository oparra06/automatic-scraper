#!/usr/bin/env python
# coding: utf-8

# In[24]:


import requests
from bs4 import BeautifulSoup
import pandas as pd


# In[25]:


response = requests.get("https://www.bbc.com/")
doc = BeautifulSoup(response.text)


# In[26]:


titles = doc.select(".media__title a")
titles


# In[9]:


for title in titles:
        print(title.text.strip())
        print(title['href'])


# In[27]:


rows = []
for title in titles:
        row['title'] = title.text.strip()
        row['url'] = title['href']
        rows.append(row)
df = pd.DataFrame(rows)
df.head()


# In[28]:


df.to_csv("bbc.csv", index=False)


# In[23]:


cd Documents


# In[ ]:




