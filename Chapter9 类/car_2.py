#!/usr/bin/env python
# coding: utf-8

# In[ ]:


"""一组用于表示燃油汽车和电动汽车的类。"""

class Car:
    """一次模拟汽车的简单尝试。"""
    def __init__(self,make,model,year):
        """初始化描述汽车的属性。"""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

        
    def get_descriptive_name(self):
        """返回整洁的描述性信息。"""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()
    
    
    def read_odometer(self):
        """打印一条指出汽车里程的信息。"""
        print(f"This car has {self.odometer_reading} miles on it.")
        
        
    def update_odometer(self,mileage):
        """
        将里程表读数设置为指定的值。
        禁止将里程表读数往回调。
        """
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")
            
            
    def increment_odometer(self,miles):
        """将里程表读数增加指定的量。"""
        self.odometer_reading += miles
        
        
    def fill_gas_tank(self):
        """打印一条指出油表的信息。"""
        print(f"The car has a gas tank.") 
        
        # 易错点：之前我在init方法中定义的是self.fil_gas_tank，运行时总是报错：'int' object is not callable
        # 后来发现是定义的函数名fill_gas_tank与self的后缀名相同导致识别矛盾
            
        
    def descriptive_battery(self):
        """打印一条描述电瓶容量的消息。"""
        print(f"This car has a {self.battery_size}-kWh battery.")
        
    
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

