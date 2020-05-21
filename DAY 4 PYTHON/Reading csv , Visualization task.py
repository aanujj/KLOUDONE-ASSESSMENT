#!/usr/bin/env python
# coding: utf-8

# In[27]:


import numpy as np


# In[28]:


import pandas as pd


# In[29]:


import seaborn as sns


# In[30]:


get_ipython().run_line_magic('matplotlib', 'inline')


# In[31]:


df1 = pd.read_csv('df1',index_col=0)


# In[32]:


df1.head()


# In[33]:


df2 = pd.read_csv('df2')


# In[34]:


df2.head()


# In[35]:


df1['A'].hist()


# In[36]:


df2.plot.bar()


# In[37]:


df2.plot.density()


# In[ ]:




