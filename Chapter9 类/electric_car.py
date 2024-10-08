#!/usr/bin/env python
# coding: utf-8

# In[ ]:


"""一组用于表示电动汽车的类。"""

from car_1 import Car
    
class Battery:
    """一次模拟电动汽车电瓶的简单尝试。"""
    def __init__(self,battery_size=75):
        """初始化电瓶的属性。"""
        self.battery_size = battery_size


    def describe_battery(self):
        """打印一条描述电瓶容量的消息。"""
        print(f"This car has a {self.battery_size}-kWh battery.")


    def get_range(self):
        """打印一条消息，指出电瓶的续航里程。"""
        if self.battery_size == 75:
            range = 260
        elif self.battery_size == 100:
            range = 315
        print(f"This car can go about {range} miles on a full charge.")

        
class ElectricCar(Car):
    """电动汽车的独特之处。"""
    def __init__(self,make,model,year):
        """
        初始化父类的属性。
        再初始化电动汽车特有的属性。
        """
        super().__init__(make,model,year) 
        self.battery = Battery()

