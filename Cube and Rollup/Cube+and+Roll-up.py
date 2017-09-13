
# coding: utf-8

# In[26]:


import numpy as np
import pandas as pd


# In[27]:


data=pd.read_csv("cube_dataset1.csv")
data


# In[28]:


data.head()


# In[29]:


pd.pivot_table(data,index=data['district'],columns=['crop_name','year'],values=['Production'],aggfunc='sum')


# In[32]:


pd.pivot_table(data,index=data['state'],columns=['district','year'],values=['Production'],aggfunc='sum')


# In[33]:


pd.pivot_table(data,index=data['year'],columns=['state','district'],values=['Production'],aggfunc='sum')


# In[ ]:




