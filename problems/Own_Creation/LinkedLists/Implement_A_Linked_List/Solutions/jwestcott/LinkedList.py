class LinkedList:

    def __init__(self):
        self.start_node: LinkedListNode = None

    def append(self, element: object):
        """Adds an element to the end of the Linked List"""
        if self.start_node is None:
            self.start_node = LinkedListNode(element)
        else:
            current_node = self.start_node
            while current_node.next_node is not None:
                current_node = current_node.next_node
            current_node.next_node = LinkedListNode(element)

    def count(self) -> int:
        """Returns the number of elements currently in the Linked List"""
        count = 0
        if self.start_node is None:
            return count
        else:
            current_node = self.start_node
            while current_node is not None:
                count += 1
                current_node = current_node.next_node
            return count


class LinkedListNode:

    def __init__(self, stored_object: object):
        self.stored_object: object = stored_object
        self.next_node: LinkedListNode = None