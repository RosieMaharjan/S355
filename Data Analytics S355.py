#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Import the needed Libraries for Pandas and Numpy
import pandas as pd
import numpy as np


# In[2]:


#Step 1 Write a module to remove dashes from a column of data (in our case it will be SSN)
def remove_dashes(x):
    remove=x.replace("-","")
    return remove


# In[147]:


#Step 2 Use the tsv file and assign it to a dataframe called S355_Data
S355_Data = pd.read_csv('S355_Final_Project_Data_TAB_Separated.txt', sep='	')


# In[148]:


#Step 3. Print the first 10 rows
print("First 10 entries:")
print("==================================================")
print(S355_Data.head(10))


# In[156]:


#Step 4. Apply the function "remove_dashes" from above to the SSN column and replace the dash values with nothing ''

#Now print the first 10 entries again to see if the dashes were removed
print("First 10 entries")
print("==================================================")
S355_Data['SSN'] = S355_Data['SSN'].apply(lambda x:remove_dashes(x))
print(S355_Data.head(10))


# In[157]:


#Step 5. What is the overall shape of observations and columns in the dataset?
# Solution 1
print("Number of Rows and Columns:")
print("==================================================")
print(S355_Data.shape)


# In[158]:


#Step 6. Print the name of all the columns.
print("Print the name of all the columns.")
print("==================================================")
print(S355_Data.columns)


# In[159]:


#Step 7. What is the data type of each column?
print("What is the data type of each column?")
print("=================================================================")
print(S355_Data.dtypes)


# In[167]:


#Step 8. Are their any duplicate Customer IDs?
#HINT: What is the most frequent CustomerID
print("What is the most frequent item_price?")
print("=================================================================")
print(S355_Data.Customer.value_counts().head())


# In[168]:


#9. Remove/Drop Duplicate CustomerIDs and then check results to make sure all duplicates are gone
S355_Data['Customer'] = S355_Data.drop_duplicates(['Customer'])
print(S355_Data.Customer.value_counts().head())


# In[65]:


#Step 10. Summarize the DataFrame. Are there any suspicious values? (i.e. K303 dreaded 9999)
print("Summarize the DataFrame.")
print("=================================================================")
print(S355_Data.describe())


# In[199]:


#Step 11. Remove rows with "bad" data.
#Remove CredCardUser = 9999 and Purchases = 9999

S355_Data['CredCardUser'] = S355_Data['CredCardUser'].replace(-9999, np.nan)
S355_Data['Purchases'] = S355_Data['Purchases'].replace(-9999, np.nan)


# In[173]:


#Step 12. RE-Summarize the DataFrame. Are there any suspicious values remaining? 
print("Summarize the DataFrame.")
print("=================================================================")
print(S355_Data.describe())


# In[175]:


#Step 13. Summarize only the Income column
print("Summarize only the Income column")
print("=================================================================")
print(S355_Data.Income.describe())


# In[177]:


#Step 14. What is the mean age of customers?
print("What is the mean age of customers?")
print("=================================================================")
S355_Data = S355_Data.rename(columns={'Current age': 'Current_age'})
print(round(S355_Data.Current_age.mean()))


# In[77]:


#Step 15. What are the Regions with most occurrence?
print("What is the Region with most occurrence?")
print("=================================================================")
print(S355_Data.Region.value_counts().head())


# In[198]:


#Step 16. Which was the total number/quantity of Purchased items?
#4368
a = S355_Data.Purchases.sum()
print(a)


# In[201]:


#Step 17. Which was the total Amount Spent on all items combined?
b = S355_Data.AmountSpent.sum()
print(b)


# In[ ]:




