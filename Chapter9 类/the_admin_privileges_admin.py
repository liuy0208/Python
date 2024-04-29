#!/usr/bin/env python
# coding: utf-8

# In[ ]:
from the_admin_user import User

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

