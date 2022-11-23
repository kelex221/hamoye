#!/usr/bin/env python
# coding: utf-8

# In[73]:


import pandas as pd
import numpy as np
URL = 'https://github.com/HamoyeHQ/HDSC-Introduction-to-Python-for-machine-learning/files/7768140/FoodBalanceSheets_E_Africa_NOFLAG.csv'
df = pd.DataFrame(pd.read_csv(URL, encoding ="latin-1"))
df.shape


# In[74]:


df.head()


# In[152]:


df[(df['Area'] == 'Madagascar') & (df['Element Code'] == 674)].groupby('Element Code').head()


# In[154]:


# What is the total Protein supply quantity in Madagascar in 2015?
df[(df['Area'] == 'Madagascar') & (df['Element Code'] == 674)].groupby('Element Code')['Y2015'].sum()


# In[196]:


# Select columns ‘Y2017’ and ‘Area’, Perform a groupby operation on ‘Area’.  Which of these Areas had the 7th lowest sum in 2017?
# Select columns ‘Y2017’ and ‘Area’, Perform a groupby operation on ‘Area’.  Which of these Areas had the highest sum in 2017?
sort_and_sum_by_Y2017 = df[['Area','Y2017']].groupby('Area')['Y2017'].sum()
sort_and_sum_by_Y2017.sort_values(ascending=False)


# In[190]:


# What is the total number of unique countries in the dataset?
no_of_countries = df.groupby('Area')['Area'].count()
print(no_of_countries.shape)
print(no_of_countries.info())


# In[223]:


# What is the total number and percentage of missing data in 2014 to 3 decimal places?
missing_data_2014 = df['Y2014'].isnull().sum()
percent_missing = missing_data_2014 * 100 / len(df)
print(round(percent_missing,3))
print(missing_data_2014)
len(df)


# In[245]:


# Perform a groupby operation on ‘Element’.  What is the total number of the sum of Processing in 2017?
processing_in_2017 = df.groupby('Element')['Y2017'].sum()
print(processing_in_2017)
sum(processing_in_2017)


# In[262]:


df[df['Item'] == 'Wine']


# In[261]:


# Answer the following questions based on the African food production dataset provided by the FAO website already provided
# What is the total sum of Wine produced in 2015 and 2018 respectively?
df[['Y2015', 'Y2018']].groupby([df['Item'] == 'Wine']).sum()


# In[268]:


# What is the mean and standard deviation across the whole dataset for the year 2017 to 2 decimal places?
df[['Y2017']].describe()


# In[288]:


# Perform a groupby operation on ‘Element’.  What year has the highest sum of Stock Variation?
df.groupby('Element')['Y2014','Y2015','Y2016','Y2017','Y2018'].describe()


# In[ ]:




