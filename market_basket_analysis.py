#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import dtale
import seaborn as sns


# In[2]:


df = pd.read_csv(r"D:\datasets\groceries - groceries.csv")
df.fillna(0, inplace=True)
df.head()


# In[3]:


x = df['Item 1'].unique()
len(x)


# In[4]:


x


# In[42]:


#zip function


# In[5]:


X = [i for i in range(1,len(x)+1)]
y = list(zip(x,X))
Y= [y[I][1] for I in range(1,158)]
y


# In[6]:


df.head()


# In[7]:


for i in range(0,158):
    df['Item 1'].replace(to_replace =str(y[i][0]),
                 value =int(y[i][1]),
              inplace = True)


# In[8]:


df[['Item 1']]


# In[17]:


df.head()


# In[13]:


df['Item 1'].unique()


# In[10]:


sns.distplot(df['Item 1'])


# In[11]:


df['Item 1'].value_counts()


# In[14]:


y


# In[17]:


y[18][0]


# In[92]:


df = pd.read_csv(r"D:\datasets\groceries - groceries.csv")
df.fillna(0, inplace=True)

df.drop('Item(s)',axis=1, inplace = True)
transactions = []


# In[91]:


type(df.values[5,5])


# In[102]:


for i in range(0, 9835):
    transactions.append([str(df.values[i,j]) for j in range(0, 32) if df.values[i,j] != 0])
    
# Creating object of apriori and setting the default values
from apyori import apriori
rules = apriori(transactions, min_support=0.003, min_confidence=0.2, min_lift=3,max_length=3)


# In[103]:


results = list(rules)
association = []
for record in results:
    association.append(list(record[0]))


# In[104]:


transactions


# In[ ]:





# In[ ]:




