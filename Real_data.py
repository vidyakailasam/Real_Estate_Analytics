#!/usr/bin/env python
# coding: utf-8

# ## BUFFALO HOUSING DATA (CURRENT ASSESSMENT ROLL 2023-2024)

# In[34]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import mpl_toolkits
get_ipython().run_line_magic('matplotlib', 'inline')


# In[35]:


data = pd.read_csv('CARfiltered2023-2024.csv', low_memory=False)
print(data.dtypes)
print("\n")
print(len(data))


# In[36]:



pd.set_option('display.max_rows', None)  # Display all rows
pd.set_option('display.max_columns', None)  # Display all columns


# In[37]:


data.head()


# In[38]:


data.describe()


# In[39]:


data['Beds'].value_counts().plot(kind='bar')
plt.title('Number of Bedroom')
plt.xlabel('Bedrooms')
plt.ylabel('Count')
sns.despine


# In[40]:


plt.figure(figsize=(20,20))
sns.jointplot(x=data.Latitude.values, y=data.Longitude.values, height=20)
plt.ylabel('Longitude', fontsize=10)
plt.xlabel('Latitude', fontsize=10)
plt.show()
sns.despine


# In[41]:


plt.scatter(data.LandValue,data.Acres)
plt.title("Land Value vs Acres")
plt.xlabel("Land Value")
plt.ylabel('Acres')


# In[42]:


plt.scatter(data.TotalValue,data.Longitude)
plt.title("Total Value vs Longitude")


# In[43]:


plt.scatter(data.TotalValue,data.Latitude)
plt.xlabel("Total Value")
plt.ylabel('Latitude')
plt.title("Latitude vs Total Value")


# In[44]:


plt.scatter(data.Beds,data.TotalValue)
plt.title("Bedroom and Value ")
plt.xlabel("No. of Beds")
plt.ylabel("Total Value")
plt.show()
sns.despine


# In[45]:


plt.scatter(data.Zipcode,data.TotalValue)
plt.title("Which is the pricey location by zipcode?")


# In[ ]:





# In[ ]:





# In[ ]:




