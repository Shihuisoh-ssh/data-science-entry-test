#!/usr/bin/env python
# coding: utf-8

# In[47]:


def find_and_replace(lst, find_val, replace_val):
    """
    Task 1
    - Create a function that searches for all occurrences of a value (find_val) in a given list (lst) and replaces them with another value (replace_val).
    - lst must be a list.
    - Return the modified list.
    """

    for x in range(len(lst)):
        if lst[x]==find_val:  #square brackets for list, this step finds the value
            lst[x] = replace_val #if found, replace with new value
               
    return lst
    


# In[49]:


# Task 2
# Invoke the function "find_and_replace" using the following scenarios:
# - [1, 2, 3, 4, 2, 2], 2, 5

list1 = [1, 2, 3, 4, 2, 2]
print(find_and_replace(list1,2,5))


# In[51]:


# Task 2
# Invoke the function "find_and_replace" using the following scenarios:
# - ["apple", "banana", "apple"], "apple", "orange"
list2 = ["apple", "banana", "apple"]
print(find_and_replace(list2,"apple","orange"))


# In[ ]:




