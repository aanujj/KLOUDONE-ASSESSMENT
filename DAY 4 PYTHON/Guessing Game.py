#!/usr/bin/env python
# coding: utf-8

# In[11]:


HiddenWord = "amazonweb"
guess = ""

Count = 0

GuessLimit = 3
ReachedLimit = False

while guess != HiddenWord and not (ReachedLimit):
    if Count < GuessLimit:
        guess = input("Enter word you guessed: ")
        Count = Count+1
    else:
        ReachedLimit = True
if ReachedLimit:
    print("You loose ,Limit Reached")
    
else:
    print("Hurray You Win huge amount")
    


# In[ ]:





# In[ ]:





# In[ ]:




