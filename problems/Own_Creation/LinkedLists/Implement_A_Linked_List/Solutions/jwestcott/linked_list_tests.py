import unittest

from LinkedList import LinkedList


class LinkedListTests(unittest.TestCase):

    def setUp(self) -> None:
        self.object_under_test = LinkedList()

    def test_LinkedList_append_correctly_sets_the_start_node_if_no_start_node_currently_exists(self) -> None:
        test_element = "test"
        self.object_under_test.append(test_element)
        self.assertIsNotNone(self.object_under_test.start_node)

    def test_LinkedList_append_adds_the_correct_data_to_the_start_node_if_no_start_node_currently_exists(self) -> None:
        test_element = "test"
        self.object_under_test.append(test_element)
        self.assertEqual(test_element, self.object_under_test.start_node.stored_object)

    def test_LinkedList_append_adds_the_correct_data_to_the_second_node_if_two_elements_are_added(self) -> None:
        for i in range(2):
            self.object_under_test.append(i)
        self.assertEqual(i, self.object_under_test.start_node.next_node.stored_object)

    def test_LinkedList_len_returns_0_if_not_elements_have_been_added(self) -> None:
        self.assertEqual(0, len(self.object_under_test))

    def test_LinkedList_len_returns_3_if_3_elements_have_been_added(self) -> None:
        for i in range(3):
            self.object_under_test.append(i)
        self.assertEqual(3, len(self.object_under_test))

    def test_LinkedList_get_raises_IndexError_if_no_elements_have_been_added(self) -> None:
        self.assertRaises(IndexError, self.object_under_test.get, 0)

    def test_LinkedList_get_raises_Index_error_if_the_desired_index_is_out_of_range(self) -> None:
        test_element = "test"
        self.object_under_test.append(test_element)
        self.assertRaises(IndexError, self.object_under_test.get, 2)

    def test_LinkedList_get_correctly_returns_the_desired_index(self) -> None:
        for i in range(1, 4):
            self.object_under_test.append("test_element_{}".format(i))
        self.assertEqual("test_element_2", self.object_under_test.get(1))

    def test_LinkedList_count_returns_0_if_there_are_no_matching_elements(self) -> None:
        for i in range(10):
            self.object_under_test.append(i)
        self.assertEqual(0, self.object_under_test.count(11))

    def test_LinkedList_count_returns_3_if_there_are_3_matching_elements(self) -> None:
        test_string = "test"
        for _ in range(3):
            self.object_under_test.append(test_string)
        self.assertEqual(3, self.object_under_test.count(test_string))


if __name__ == "__main__":
    unittest.main()
