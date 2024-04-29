#!/usr/bin/env python
# coding: utf-8

# In[ ]:
"""模拟用户与管理员的简单尝试。"""

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
        
        
    def greet_user(self):
        """向用户发送一条个性的问候。"""
        user_name = f"{self.first_name.title()} {self.last_name.title()}"
        print(f"Nice to meet you,{user_name.title()}!")
        

class Privileges:
    """模拟管理员权限的简单测试。"""
    def __init__(self):
        """初始化属性"""
        self.privileges = ['can add post','can delete post','can ban user']


    def show_privileges(self):
        """显示管理员的权限"""
        print(f"Admin has following privileges:")
        for privilege in self.privileges:
            print(privilege)

        
class Admin(User):
    """一次模拟管理员的简单尝试。"""
    def __init__(self,first_name,last_name,age,location):
        """
        初始化父类的属性。
        并初始化管理员特有的属性。
        """
        super().__init__(first_name,last_name,age,location)
        self.privileges_admin = Privileges() 