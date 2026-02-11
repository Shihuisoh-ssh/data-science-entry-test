#!/usr/bin/env python
# coding: utf-8

# In[13]:


class Car:
    """
    Task 1
    - Define a class named Car with attributes: make, model, year
    - Initialize these attributes in the __init__ method
    - Add a method named describe_car() that prints information about the car as "Year Make Model"
    """
    def __init__(self,make, model, year):
        self.make =make # using self to access class properties
        self.model= model
        self.year = year

    def describe_car(self):
        
        print(f"{self.year} {self.make} {self.model}")




# In[15]:


# Task 2
# Create an instance of the Car class with the following attributes and call describe_car method:
# - Make: Toyota, Model: Corolla, Year: 2020

data = Car("Toyota", "Corrolla", 2020)
data.describe_car()


# In[ ]:




