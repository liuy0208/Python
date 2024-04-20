#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def make_pizza(size,*toppings):
    """概述要制作的披萨。"""
    print(f"\nMaking a {size}-inch pizza with the following toppings: ")
    for topping in toppings:
        print(f"-{topping}")

        
def build_profile(manufacture,model,**car_info):
    car_info['manufacture'] = manufacture
    car_info['model'] = model
    return car_info