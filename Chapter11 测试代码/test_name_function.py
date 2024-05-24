import unittest
from name_function import get_formatted_name
class NameTestCase(unittest.TestCase):
    """测试name_function.py。"""

    def test_first_last_name(self):
        """能够正确地处理像Janis Joplin这样的姓名吗？"""
        formatted_name = get_formatted_name('Janis','joplin')
        self.assertEqual(formatted_name,'Janis Joplin')
    
    def test_first_middle_last_name(self):
        """能够正确地处理像Wolfgang Amadeus Mozart这样的名字吗？"""
        formatted_name = get_formatted_name('wolfgang','mozart','amadeus')
        self.assertEqual(formatted_name,'Wolfgang Amadeus Mozart')

# 下面的if语句不在NameTestCase类当中，如果缩进了不会被检测到，将无法测试代码。将会被提示，发生了SystemExit异常
if __name__ == '__main__':
    unittest.main()