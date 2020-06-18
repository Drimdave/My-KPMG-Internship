#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')


# In[2]:


trans = pd.read_excel(r"C:\Users\seyi\Desktop\My Internship Work\KPMG INTERNSHIP\transaction dataset.xlsx") 


# In[3]:


trans.head()


# In[4]:


trans.shape


# In[5]:


trans.describe()


# In[6]:


trans.isnull().sum()


# In[7]:


trans['online_order'].value_counts()


# In[8]:


trans['online_order']=trans['online_order'].fillna(method='ffill')


# In[10]:


trans['brand'].value_counts()


# In[11]:


trans['brand']=trans['brand'].fillna(method='ffill')


# In[12]:


trans['product_line'].value_counts()


# In[13]:


trans['product_line']=trans['product_line'].fillna(method='ffill')


# In[14]:


trans['product_class'].value_counts()


# In[15]:


trans['product_class']=trans['product_class'].fillna(method='ffill')


# In[16]:


trans['product_size'].value_counts()


# In[17]:


trans['product_size']=trans['product_size'].fillna(method='ffill')


# In[18]:


trans['standard_cost'].mean()


# In[19]:


trans['standard_cost']=trans['standard_cost'].fillna(trans['standard_cost'].mean())


# In[20]:


trans['product_first_sold_date']=trans['product_first_sold_date'].fillna(trans['product_first_sold_date'].mean())


# In[22]:


submission = pd.DataFrame({
        "transaction_id": trans["transaction_id"],
        "product_id": trans["product_id"],
        "customer_id": trans["customer_id"],
        "transaction_date": trans["transaction_date"],
        "online_order": trans["online_order"],
        "order_status": trans["order_status"],
        "brand": trans["brand"],
        "product_line": trans["product_line"],
        "product_class": trans["product_class"],
        "product_size": trans["product_size"],
        "list_price": trans["list_price"],
        "standard_cost": trans["standard_cost"],
        "product_first_sold_date": trans["product_first_sold_date"]
    })
submission.to_csv('./submission.csv', index=False)


# In[23]:


submission.head()


# In[24]:


submission.describe()


# It can be seen that all the missing values have been filled.

# In[ ]:




