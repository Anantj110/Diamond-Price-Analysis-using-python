#!/usr/bin/env python
# coding: utf-8

# In[ ]:


cut------------Quality of the cut (Fair, Good, Very Good, Premium, Ideal)
color----------Diamond colour, from J (worst) to D (best)
clarity---------How clear the diamond is (I1 (worst), SI2, SI1, VS2, VS1, VVS2, VVS1, IF(best))


# In[32]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# In[33]:


df = pd.read_csv('D:\downloads\diamonds.csv\diamonds.csv')
df.head()


# In[34]:


df.shape


# In[35]:


df.info()


# In[36]:


df.describe()


# In[37]:


print(df.cut.value_counts(), '\n', df.clarity.value_counts(), '\n', df.color.value_counts())


# In[38]:


df.head(10)


# In[39]:


sns.histplot(df['price'], bins=30)


# In[40]:


sns.histplot(df['carat'], bins=30)


# In[ ]:


Most of the Diamond are under 1 carat in weight


# In[42]:


plt.figure(figsize=(6,6))
plt.pie(df['cut'].value_counts(), labels=['Premium', 'Very good', 'Good', 'Ideal', 'Fair'])
plt.title('cut')
plt.show()


# In[43]:


plt.bar(df['color'].value_counts().index, df['color'].value_counts())
plt.ylabel('Number of diamonds')
plt.xlabel('color')
plt.show()


# In[44]:


plt.bar(df['clarity'].value_counts().index, df['clarity'].value_counts())
plt.title('Clarity')
plt.ylabel('No. of Diamonds')
plt.xlabel('Clarity')


# In[45]:


plt.hist(df['table'], bins=20)


# In[46]:


plt.figure(figsize=(6,6))
sns.barplot(x='cut', y='price', data=df)


# In[47]:


plt.figure(figsize=(6,6))
sns.barplot(x='color', y='price', data=df)


# In[48]:


sns.set(rc={'figure.figsize': (6, 6)})
sns.barplot(x='clarity', y='price', data=df)


# In[49]:


#changing categorical variables to numerical variables
df['cut'] = df['cut'].map({'Ideal':5,'Premium':4,'Very Good':3,'Good':2,'Fair':1})
df['color'] = df['color'].map({'D':7,'E':6,'F':5,'G':4,'H':3,'I':2,'J':1})
df['clarity'] = df['clarity'].map({'IF':8,'VVS1':7,'VVS2':6,'VS1':5,'VS2':4,'SI1':3, 'SI2':2, 'IF':1})


# In[50]:


df.corr()


# In[51]:


sns.lineplot(x='carat',y='price',data=df)
plt.title('Carat vs Price')
plt.show()


# In[52]:


plt.plot(df['carat'], df['price'])
plt.xlabel('Carat')
plt.ylabel('Price')
plt.title('Line Plot of Carat vs Price')
plt.show()


# In[ ]:


From the lineplot it is quite clear that the price of the diamond increases with the increase in the carat of the diamond. 
However, diamonds with less carat also have high price. This is because of the other factors that affect the price of the 
diamond.


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


As i have converted the categorical variables to numerical variables it will allow us to make it more easy for us to 
analyze it further.

