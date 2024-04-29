#!/usr/bin/env python
# coding: utf-8

# In[ ]:


class User:
    """一次模拟收集用户信息与发出问候的测试。"""
    def __init__(self,first_name,last_name,age,location):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.location = location
        
        
    def describe_user(self):
        """描述用户基本信息。"""
        print("User's information is following:")
        print(f"first name: {self.first_name}")
        print(f"last name:{self.last_name}")
        print(f"age:{self.age}")
        print(f"location:{self.location}")

