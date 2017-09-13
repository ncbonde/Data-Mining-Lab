
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd


# In[35]:


data=map(int,raw_input("Enter the data:-").split())


# In[36]:


min(data)


# In[37]:


max(data)


# In[38]:


data.sort()
data


# In[39]:


def q1(data):
    a=len(data)*0.25
    if(a==int(a)):
        print data[int(a)]
    else:
        print (data[int(a)]+data[int(a+1)])/2.0
    


# In[40]:


q1(data)


# In[41]:


def q2(data):
    a=len(data)*0.5
    if(a==int(a)):
        print data[int(a)]
    else:
        print (data[int(a)]+data[int(a+1)])/2.0
    


# In[42]:


def q3(data):
    a=len(data)*0.75
    if(a==int(a)):
        print data[int(a)]
    else:
        print (data[int(a)]+data[int(a+1)])/2.0
    


# In[43]:


q2(data)


# In[44]:


q3(data)


# In[ ]:




