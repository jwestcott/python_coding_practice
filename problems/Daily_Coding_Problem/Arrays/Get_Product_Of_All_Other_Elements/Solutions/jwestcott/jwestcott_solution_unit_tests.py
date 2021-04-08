import unittest

import jwestcott_solution_original as orig
import jwestcott_solution_no_division as no_div
import jwestcott_solution_pre_computed as pre_comp


class TestProductOfAllOtherElements(unittest.TestCase):

    def test_product_of_all_other_elements_original_implementation(self):
        self.assertEqual([120, 60, 40, 30, 24], orig.product_of_all_other_elements([1, 2, 3, 4, 5]))
        self.assertEqual([2, 3, 6], orig.product_of_all_other_elements([3, 2, 1]))

    def test_product_of_all_other_elements_no_division_implementation(self):
        self.assertEqual([120, 60, 40, 30, 24], no_div.product_of_all_other_elements([1, 2, 3, 4, 5]))
        self.assertEqual([2, 3, 6], no_div.product_of_all_other_elements([3, 2, 1]))

    def test_product_of_all_other_elements_pre_computed_implementation(self):
        self.assertEqual([120, 60, 40, 30, 24], pre_comp.product_of_all_other_elements([1, 2, 3, 4, 5]))
        self.assertEqual([2, 3, 6], pre_comp.product_of_all_other_elements([3, 2, 1]))


if __name__ == "__main__":
    unittest.main()
