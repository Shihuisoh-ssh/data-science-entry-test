#!/usr/bin/env python
# coding: utf-8

# In[1]:


def string_reverse(s):
    """
    Task 1
    - Create a function that reverses a given string (s).
    - s must be a string.
    - Return the reversed string. 
    (hi I am not sure what this means. Do we want to reverse "Good Day" to "yaD dooG" or "Day Good"? I have done the first option)
    """
    # checking for string
    if not isinstance(s,str):
        raise TypeError("Pls key in a string")
            
    return s[::-1]



# In[3]:


# Task 2
# Invoke the function "string_reverse" using the following scenarios:
# - "Hello World"
print(string_reverse("Hello World"))


# In[5]:


# Task 2
# Invoke the function "string_reverse" using the following scenarios:
# - "Python"
print(string_reverse("Python"))


# In[ ]:




