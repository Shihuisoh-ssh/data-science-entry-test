#!/usr/bin/env python
# coding: utf-8

# In[1]:


def swap(x,y):
    """
    Task 1
    - Create a function that would swap the value of x and y using only x and y as variables.
    - x and y must be numeric.
    - Return -1 if x and y is not numeric, and
    - print the swapped values if both x and y are numeric.
    """
    if type(x)!= int and type(x)!=float: 
        return -1
    elif type(y)!=int and type(y)!=float:
        return -1
    else:
        x_newvariable = x
        x = y
        y = x_newvariable
        print (x,y)
        return
        
        


# In[3]:


# Task 2
# Invoke the function "swap" using the following scenarios:
# - "Apple", 10

swap("Apple",10)


# In[5]:


# Task 2
# Invoke the function "swap" using the following scenarios:
# - 9, 17

swap(9,17)


# In[ ]:




