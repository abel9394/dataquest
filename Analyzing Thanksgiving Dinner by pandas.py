
# coding: utf-8

# In[18]:

import pandas as pd
import re
data = pd.read_csv("thanksgiving.csv", encoding="Latin-1")
data.head()


# In[2]:

print(data.columns)


# In[4]:

data["Do you celebrate Thanksgiving?"].value_counts()


# In[8]:

newdata = data[data["Do you celebrate Thanksgiving?"]=="Yes"]


# In[9]:

newdata.head()


# In[11]:

newdata["What is typically the main dish at your Thanksgiving dinner?"].value_counts()


# In[12]:

newdata_Tofurkey = newdata[newdata["What is typically the main dish at your Thanksgiving dinner?"]=="Tofurkey"]


# In[13]:

newdata_Tofurkey["Do you typically have gravy?"]


# In[14]:

apple_isnull = newdata["Which type of pie is typically served at your Thanksgiving dinner? Please select all that apply. - Apple"].isnull()


# In[15]:

apple_isnull.head()


# In[17]:

pumpkin_isnull = newdata["Which type of pie is typically served at your Thanksgiving dinner? Please select all that apply. - Pumpkin"].isnull()
pecan_isnull = newdata["Which type of pie is typically served at your Thanksgiving dinner? Please select all that apply. - Pecan"].isnull()
ate_pies = apple_isnull&pumpkin_isnull&pecan_isnull
ate_pies.value_counts()


# In[24]:

def age_correction(column):
    if pd.isnull(column):
        return None
    else:
        newage = re.split('-|\+',column)[0]
        return int(newage)
newdata["int_age"]=newdata["Age"].apply(age_correction)
newdata["int_age"].describe()
    
    


# In[32]:

def money_correction(column):
    
    if pd.isnull(column):
        return None  
    column=column.split(" ")[0]
    if column=="Prefer":
        return None
    else:          
        newmoney = re.sub("\$|,","",column)
        return int(newmoney)
newdata["int_income"]=newdata["How much total combined money did all members of your HOUSEHOLD earn last year?"].apply(money_correction)
newdata["int_income"].describe()



# In[36]:

newdata_lowincome = newdata["int_income"]<50000
newdata.loc[newdata_lowincome,"How far will you travel for Thanksgiving?"].value_counts()


# In[38]:

newdata.loc[newdata["int_income"]>150000,"How far will you travel for Thanksgiving?"].value_counts()


# In[39]:

newdata_table = newdata.pivot_table(index="Have you ever tried to meet up with hometown friends on Thanksgiving night?",columns='Have you ever attended a "Friendsgiving?"',values="int_age")
print(newdata_table)


# In[40]:

newdata_table = newdata.pivot_table(index="Have you ever tried to meet up with hometown friends on Thanksgiving night?",columns='Have you ever attended a "Friendsgiving?"',values="int_income")
print(newdata_table)


# In[ ]:



