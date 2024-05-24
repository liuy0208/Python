class Employee:
    """收集雇员可增加的年薪值。"""
    def __init__(self,first_name,last_name,annual_salary):
        """初始化雇员的名、姓与年薪。"""
        self.first_name = first_name.title()
        self.last_name = last_name.title()
        self.salary = annual_salary
    
    def give_raise(self,raise_value=5000):
        """打印该雇员最终的年薪。"""
        self.salary += raise_value
        return self.salary
        