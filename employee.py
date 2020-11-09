#!/usr/bin/env python
# coding: utf-8

# In[ ]:


class Employee:
    def __init__(self, first_name, last_name, annual_salary):
        self.__first_name = first_name
        self.__last_name = last_name
        self.__annual_salary = annual_salary   
     
    def get_name(self):
        return self.__first_name
    
    def get_last(self):
        return self.__last_name
    
    def get_salary(self):
        return self.__annual_salary
    
    def give_raise(self, raise_rate = 0.02):
        return self.__annual_salary*raise_rate
    
   

