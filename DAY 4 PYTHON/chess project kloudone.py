#!/usr/bin/env python
# coding: utf-8

# In[1]:


import chess  #install library first pip install python-chess 


# In[2]:


board = chess.Board()


# In[3]:


board


# In[4]:


board.legal_moves 


# In[5]:


chess.Move.from_uci("a8a1") in board.legal_moves


# In[6]:


board.push_san("e4") #to make a move


# In[ ]:





# In[7]:


board.push_san("e5")


# In[8]:


board


# In[9]:


board.push_san("Qh5")


# In[ ]:





# In[ ]:





# In[10]:


board


# In[ ]:





# In[11]:


board.push_san("Nc6")


# In[12]:


board


# In[13]:


board.push_san("Bc4")


# In[14]:


board


# In[15]:


board.push_san("Nf6")


# In[16]:


board


# In[17]:


board.push_san("Qxf7")


# In[ ]:





# In[18]:


board


# In[ ]:





# In[19]:


board.is_checkmate()


# In[20]:


board


# In[21]:


board.is_game_over()


# In[ ]:




