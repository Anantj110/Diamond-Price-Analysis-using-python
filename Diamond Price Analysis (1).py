#!/usr/bin/env python
# coding: utf-8

# In[ ]:


cut------------Quality of the cut (Fair, Good, Very Good, Premium, Ideal)
color----------Diamond colour, from J (worst) to D (best)
clarity---------How clear the diamond is (I1 (worst), SI2, SI1, VS2, VS1, VVS2, VVS1, IF(best))


# In[2]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# In[4]:


df = pd.read_csv('D:\downloads\diamonds.csv\diamonds.csv')
df.head()


# In[5]:


df.shape


# In[6]:


df.info()


# In[7]:


df.describe()


# In[8]:


print(df.cut.value_counts(), '\n', df.clarity.value_counts(), '\n', df.color.value_counts())


# In[9]:


df.head(10)


# In[10]:


sns.histplot(df['price'], bins=30)


# In[11]:


sns.histplot(df['carat'], bins=30)


# In[ ]:


Most of the Diamond are under 1 carat in weight


# In[13]:


plt.figure(figsize=(6,6))
plt.pie(df['cut'].value_counts(), labels=['Premium', 'Very good', 'Good', 'Ideal', 'Fair'])
plt.title('cut')
plt.show()


# In[14]:


plt.bar(df['color'].value_counts().index, df['color'].value_counts())
plt.ylabel('Number of diamonds')
plt.xlabel('color')
plt.show()


# In[15]:


plt.bar(df['clarity'].value_counts().index, df['clarity'].value_counts())
plt.title('Clarity')
plt.ylabel('No. of Diamonds')
plt.xlabel('Clarity')


# In[16]:


plt.hist(df['table'], bins=20)


# In[24]:


plt.figure(figsize=(6,6))
sns.barplot(x='cut', y='price', data=df)


# In[20]:


plt.figure(figsize=(6,6))
sns.barplot(x='color', y='price', data=df)


# In[23]:


sns.set(rc={'figure.figsize': (6, 6)})
sns.barplot(x='clarity', y='price', data=df)


# In[ ]:


J color and I1 clarity are worst featiures for a diamond, however when the data is plotted on bar graph, 
it is seen that the price of diamonds with J color and I1 clarity is higher than the price of diamonds 
with D color and IF clarity, which is opposite to what I expected


# In[ ]:


There is something interesting about the data. The price of the diamonds with J color
and I1 clarity is higher than the price of the diamonds with D color and IF clarity which
couldn't be explained by the models. This could be because of the other factors that
affect the price of the diamond.


# In[ ]:




