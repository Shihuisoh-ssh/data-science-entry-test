#!/usr/bin/env python
# coding: utf-8

# In[1]:


def find_first_negative(lst):
    """
    Task 1
    - Create a function that finds the first negative number in a list (lst).
    - Return the first negative number if found, otherwise return "No negatives".
    - Use a while loop to implement this.
    """
    i = 0  # start with index 0
    while i < len(lst): # when index is less than total no of items
        if lst[i] < 0: #checks and return the result immediately if it is negative
            return lst[i]
        i += 1
    return "No negatives"
      




# In[3]:


# Task 2
# Invoke the function "find_first_negative" using the following scenario:
# - [3, 5, -1, 7, -2, 8]
data1=[3, 5, -1, 7, -2, 8]
print(find_first_negative(data1))


# In[5]:


# Task 2
# Invoke the function "find_first_negative" using the following scenario:
# - [2, 10, 7, 0]

data2=[2, 10, 7, 0]
print(find_first_negative(data2))


# In[ ]:




