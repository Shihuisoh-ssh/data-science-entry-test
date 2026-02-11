#!/usr/bin/env python
# coding: utf-8

# In[35]:


def update_dictionary(dct, key, value):
    """
    Task 1
    - Create a function that updates a dictionary (dct) with a new key-value pair.
    - If the key already exists in dct, print the original value, then update its value.
    - Return the updated dictionary.
    """
    # loop through dictionary keys
    for x in dct:
        if x == key:
            dct[x]=value
            return dct
            
    # if key is not found in the loop
    dct[key]=value
    
    return dct



# In[37]:


# Task 2
# Invoke the function "update_dictionary" using the following scenarios:
# - {}, "name", "Alice"
# - {"age": 25}, "age", 26

personal_data = {"name":"Alice","age":25}
print (personal_data)


# In[39]:


new_personal_data = update_dictionary(personal_data, "age", 26)
print(new_personal_data)


# In[ ]:




