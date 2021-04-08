class LinkedList:

    def __init__(self):
        self.start_node: LinkedListNode = None

    def append(self, element: object) -> None:
        """Adds an element to the end of the Linked List"""
        if self.start_node is None:
            self.start_node = LinkedListNode(element)
        else:
            current_node = self.start_node
            while current_node.next_node is not None:
                current_node = current_node.next_node
            current_node.next_node = LinkedListNode(element)

    def count(self, element: object) -> int:
        """Returns the number of elements with the passed value"""
        count = 0
        current_node = self.start_node
        while current_node is not None:
            if current_node.stored_object == element:
                count += 1
            current_node = current_node.next_node
        return count

    def get(self, index: int) -> object:
        """Returns the element of the Linked List at the passed index"""
        if self.start_node is None:
            raise IndexError("LinkedList is currently empty")
        current_node = self.start_node
        for _ in range(index):
            if current_node is None:
                raise IndexError("Index is out of bounds")
            else:
                current_node = current_node.next_node
        return current_node.stored_object

    def __len__(self) -> int:
        """Returns the number of elements currently in the Linked List"""
        count = 0
        current_node = self.start_node
        while current_node is not None:
            count += 1
            current_node = current_node.next_node
        return count

    def __repr__(self) -> str:
        """Provides a string representation of the LinkedList"""
        start_string = "LinkedList(["
        contents_string = ""
        current_node = self.start_node
        while current_node is not None:
            contents_string += "{},".format(current_node.stored_object)
            current_node = current_node.next_node
        end_string = "])"
        return start_string + contents_string[:-1] + end_string


class LinkedListNode:

    def __init__(self, stored_object: object):
        self.stored_object: object = stored_object
        self.next_node: LinkedListNode = None
