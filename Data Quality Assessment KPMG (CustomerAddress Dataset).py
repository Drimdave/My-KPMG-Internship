#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')


# In[2]:


custadd = pd.read_excel(r"C:\Users\seyi\Desktop\My Internship Work\KPMG INTERNSHIP\customer address.xlsx")


# In[3]:


custadd.head()


# In[4]:


custadd.shape


# In[5]:


custadd.describe()


# In[6]:


custadd.isnull().sum()


# In[12]:


custadd['address'].value_counts()


# In[13]:


custadd['postcode'].value_counts()


# In[7]:


custadd['postcode'].plot()


# In[14]:


custadd['state'].value_counts()


# In[15]:


custadd['country'].value_counts()


# In[16]:


custadd['property_valuation'].value_counts()


# In[10]:


custadd['property_valuation'].plot()


# In[17]:


submission = pd.DataFrame({
        "customer_id": custadd["customer_id"],
        "address": custadd["address"],
        "postcode": custadd["postcode"],
        "state": custadd["state"],
        "country": custadd["country"],
        "property_valuation": custadd["property_valuation"]
    })
submission.to_csv('./submission.csv', index=False)


# In[18]:


submission.head()


# In[19]:


submission.describe()

