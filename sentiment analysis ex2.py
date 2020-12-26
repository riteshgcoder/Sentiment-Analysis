#!/usr/bin/env python
# coding: utf-8

# In[1]:


from textblob import TextBlob


# In[12]:


y=input('Type your message:')
ritesh=TextBlob(y)
x=ritesh.sentiment.polarity
# -ve=x<0 and neutral=0 and +ve x>0 && x<=1
if x<0:
    print('Negative')
elif x==0:
    print('Neutral')
elif x>0 and x<=1:
    print('Positive')


#Output:-
Type your message:she is beautiful
Positive




