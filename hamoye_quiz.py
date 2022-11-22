#!/usr/bin/env python
# coding: utf-8

# In[10]:


import pandas as pd
import numpy as np
URL = 'https://github.com/HamoyeHQ/HDSC-Introduction-to-Python-for-machine-learning/files/7768140/FoodBalanceSheets_E_Africa_NOFLAG.csv'
df = pd.read_csv(URL, encoding ="latin-1")
df.shape


# In[11]:


df.head()


# In[71]:


df[['Y2017','Area']].


# In[30]:


df.groupby('Element code')['Element code'].sum()


# In[27]:


df.describe()


# In[31]:


my_tuppy = (1,2,5,8)

my_tuppy[2] = 6


# In[66]:





# In[ ]:




