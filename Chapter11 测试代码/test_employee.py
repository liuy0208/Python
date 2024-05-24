import unittest
from employee import Employee
class TestEmployee(unittest.TestCase):
    """测试employee.py。"""
    def setUp(self):
        """创建一个默认的年薪增量和一个非默认年薪增量下的最终年薪，供使用的测试方法使用。"""
        self.employee = Employee('Bowen','Wang',100000)

    def test_give_default_raise(self):
        """测试增加非默认年薪增量后的年薪。"""
        self.employee.give_raise(10000)
        self.assertEqual(self.employee.salary,110000)

    def test_give_custom_raise(self):
        """测试增加默认年薪增量后的年薪。"""
        self.employee.give_raise()
        self.assertEqual(self.employee.salary,105000)

if __name__ == '__main__':
    unittest.main()