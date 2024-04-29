#!/usr/bin/env python
# coding: utf-8

# In[ ]:
"""模拟餐馆和冰激凌小店的尝试。"""

class Restaurant:
    """一次模拟餐馆的简单测试。"""
    def __init__(self,restaurant_name,cuisine_type):
        """初始化属性restaurant_name和cuisine_type。"""
        self.name = restaurant_name
        self.type = cuisine_type
    
    
    def describe_restaurant(self):
        """描述餐馆名称与菜肴类型"""
        print(f"This restaurant'name is {self.name}")
        print(f"This restaurant's cuisine-type is {self.type}")
    
    
    def open_restaurant(self):
        """指出餐馆正在营业"""
        print(f"{self.name.title()} is opening now.")
        

class IceCreamStand(Restaurant):
    """模拟冰激凌小店。"""
    def __innit__(self,restaurant_name,cuisine_type):
        """
        初始化父类的属性。
        再初始化冰激凌小店的属性。
        """
        super().__init__(restaurant_name,cuisine_type)
        self.flavors = []
        
    
    def save_icecream_flavors(self,*flavors):
        """存储冰激凌的口味。"""
        self.flavors = [*flavors]
        print(self.flavors)
        
        
    def describe_icecream_flavors(self):
        """显示冰激凌的口味。"""
        print("We provide following flavors:")
        for flavor in self.flavors:
            print(flavor)

