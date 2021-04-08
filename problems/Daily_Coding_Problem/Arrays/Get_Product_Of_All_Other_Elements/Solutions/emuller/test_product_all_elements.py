from Product_All_Elements import *
import unittest


class TestProduct(unittest.TestCase):

    def test_product(self):
        self.assertEqual(product_elements([1, 2, 3, 4, 5]), [120.0, 60.0, 40.0, 30.0, 24.0])
        self.assertEqual(product_elements([3, 20, 1]), [20.0, 3.0, 60.0])

    def test_product_v2(self):
        self.assertEqual(product_elements_v2([1, 2, 3, 4, 5]), [120, 60, 40, 30, 24])
        self.assertEqual(product_elements_v2([3, 20, 1]), [20.0, 3.0, 60.0])
