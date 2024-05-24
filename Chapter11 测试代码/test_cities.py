import unittest
from city_functions import get_city_country_relation
class RelationTestCase(unittest.TestCase):
    """测试city_functions.py。"""

    def test_city_country(self):
        """测试是否能够返回像‘Santiago，Chile’这样的关系值。"""
        city_country = get_city_country_relation('santiago','chile')
        self.assertEqual(city_country,'Santiago,Chile')

    def test_city_country_population(self):
        """测试是否能够返回像‘Santiago，CHile - population 5000000’这样的格式。"""
        city_country = get_city_country_relation('santiago','chile',5000000)
        self.assertEqual(city_country,'Santiago,Chile - population 5000000')

if __name__ == '__main__':
    unittest.main()