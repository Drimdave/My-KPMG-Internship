#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd


# In[2]:


ncl = pd.read_excel(r"C:\Users\seyi\Desktop\My Internship Work\KPMG INTERNSHIP\new customer list.xlsx")


# In[3]:


ncl.head()


# In[4]:


ncl.shape


# In[7]:


ncl.describe()


# In[8]:


ncl.isnull().sum()


# In[9]:


ncl['last_name'].value_counts()


# In[10]:


ncl['last_name']=ncl['last_name'].fillna(method='ffill')


# In[11]:


ncl['DOB'].value_counts()


# In[12]:


ncl['DOB']=ncl['DOB'].fillna(method='ffill')


# In[14]:


ncl['job_title'].value_counts()


# In[15]:


ncl['job_title']=ncl['job_title'].fillna(method='ffill')


# In[16]:


ncl['job_industry_category'].value_counts()


# In[17]:


ncl['job_industry_category']=ncl['job_industry_category'].fillna(method='ffill')


# In[18]:


submission = pd.DataFrame({
        "first_name": ncl["first_name"],
        "last_name": ncl["last_name"],
        "gender": ncl["gender"],
        "past_3_years_bike_related_purchases": ncl["past_3_years_bike_related_purchases"],
        "DOB": ncl["DOB"],
        "job_title": ncl["job_title"],
        "job_industry_category": ncl["job_industry_category"],
        "wealth_segment": ncl["wealth_segment"],
        "deceased_indicator": ncl["deceased_indicator"],
        "owns_car": ncl["owns_car"],
        "tenure": ncl["tenure"],
        "address": ncl["address"],
        "postcode": ncl["postcode"],
        "state": ncl["state"],
        "country": ncl["country"],
        "property_valuation": ncl["property_valuation"],
        "Rank": ncl["Rank"],
        "Value": ncl["Value"]
    })
submission.to_csv('./submission.csv', index=False)


# In[19]:


submission.head()


# In[20]:


submission.describe()

