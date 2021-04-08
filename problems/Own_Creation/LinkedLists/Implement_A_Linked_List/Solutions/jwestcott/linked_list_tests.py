import unittest

from LinkedList import LinkedList


class LinkedListTests(unittest.TestCase):

    def setUp(self) -> None:
        self.object_under_test = LinkedList()

    def test_LinkedList_append_correctly_sets_the_start_node_if_no_start_node_currently_exists(self):
        test_element = "test"
        self.object_under_test.append(test_element)
        self.assertIsNotNone(self.object_under_test.start_node)

    def test_LinkedList_append_adds_the_correct_data_to_the_start_node_if_no_start_node_currently_exists(self):
        test_element = "test"
        self.object_under_test.append(test_element)
        self.assertEqual(test_element, self.object_under_test.start_node.stored_object)

    def test_LinkedList_append_adds_the_correct_data_to_the_second_node_if_two_elements_are_added(self):
        for i in range(2):
            self.object_under_test.append(i)
        self.assertEqual(i, self.object_under_test.start_node.next_node.stored_object)

    def test_LinkedList_count_returns_0_if_not_elements_have_been_added(self):
        self.assertEqual(0, self.object_under_test.count())

    def test_LinkedList_count_returns_3_if_3_elements_have_been_added(self):
        for i in range(3):
            self.object_under_test.append(i)
        self.assertEqual(3, self.object_under_test.count())


if __name__ == "__main__":
    unittest.main()
