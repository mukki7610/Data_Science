
# coding: utf-8

# #### list

# In[1]:


my_list_1 = ["a","b","c","d","e"]


# In[2]:


my_list_1


# In[3]:


my_list_2 = [100,200,56,67,89]


# In[4]:


print(my_list_2)


# In[5]:


my_list_1[2]


# In[7]:


my_list_1[3]


# In[8]:


my_list_2[4]


# In[9]:


my_list_1[2:5]


# In[10]:


my_list_1[1:4]


# In[11]:


my_list_2[:5]


# In[12]:


my_list_2[-3] = 200


# In[13]:


my_list_2


# ## slicing in list

# In[14]:


my_list_2.append('900')


# In[15]:


print(my_list_2)


# In[16]:


my_list_3 =[100,200,10,400,500,100]


# In[18]:


print(my_list_3)


# In[19]:


my_list_1.extend(my_list_3)


# In[20]:


print(my_list_1,my_list_3)

