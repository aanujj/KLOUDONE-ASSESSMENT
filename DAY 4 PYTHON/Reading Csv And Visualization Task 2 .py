#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


import matplotlib.pyplot as plt


# In[3]:


get_ipython().run_line_magic('matplotlib', 'inline')


# In[4]:


df3 = pd.read_csv('df3')


# In[5]:


df3.head()


# In[6]:


df3.plot.scatter(x='a',y='c')


# In[7]:


df3['a'].plot.hist(bins=20)


# In[8]:


df3[['a','b']].plot.box()


# In[9]:


df3['d'].plot.kde(ls='--')


# In[11]:


df3[0:30].plot.area(alpha=0.4)


# In[ ]:




