
# coding: utf-8

# In[3]:


import numpy as np
import pandas as pd


# In[4]:


data=pd.read_csv("twtdwt.csv")


# In[8]:


data


# get total Employee

# In[6]:


data['Total']=data['Male']+data['Female']  


# In[9]:


data


# # t-weight

# In[10]:


data['Male_t-weight']=data['Male']/data['Total']
data['Female_t-weight']=data['Female']/data['Total']


# In[11]:


data


# # d-weight

# In[12]:


data['Male_d-weight']=data['Male']/sum(data['Total'])
data['Female_d-weight']=data['Female']/sum(data['Total'])


# In[13]:


data


# In[ ]:




