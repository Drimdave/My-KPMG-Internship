#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd


# In[2]:


custd = pd.read_excel(r"C:\Users\seyi\Desktop\My Internship Work\KPMG INTERNSHIP\customer demographic.xlsx")


# In[3]:


custd.head()


# In[4]:


custd.shape


# In[6]:


custd.describe()


# In[7]:


custd.isnull().sum()


# In[8]:


custd['last_name'].value_counts()


# In[9]:


custd['last_name']=custd['last_name'].fillna(method='ffill')


# In[10]:


custd['DOB'].value_counts()


# In[12]:


custd['DOB']=custd['DOB'].fillna(method='ffill')


# In[14]:


custd['job_title'].value_counts()


# In[15]:


custd['job_title']=custd['job_title'].fillna(method='ffill')


# In[16]:


custd['job_industry_category'].value_counts()


# In[17]:


custd['job_industry_category']=custd['job_industry_category'].fillna(method='ffill')


# In[18]:


del custd['default']


# In[19]:


custd['tenure'].mean()


# In[20]:


custd['tenure']=custd['tenure'].fillna(method='ffill')


# In[21]:


submission = pd.DataFrame({
        "customer_id": custd["customer_id"],
        "first_name": custd["first_name"],
        "last_name": custd["last_name"],
        "gender": custd["gender"],
        "past_3_years_bike_related_purchases": custd["past_3_years_bike_related_purchases"],
        "DOB": custd["DOB"],
        "job_title": custd["job_title"],
        "job_industry_category": custd["job_industry_category"],
        "wealth_segment": custd["wealth_segment"],
        "deceased_indicator": custd["deceased_indicator"],
        "owns_car": custd["owns_car"],
        "tenure": custd["tenure"]
    })
submission.to_csv('./submission.csv', index=False)


# In[22]:


submission.head()


# In[24]:


submission.describe()


# In[ ]:




