class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        currentNode = self.head
        if currentNode == None:
            newNode = Node(data)
        else:
            while currentNode.next != None:
                currentNode = currentNode.next
            currentNode.next = Node(data)

    def count(self, n):
        currentNode = self.head
        count = 0
        while currentNode != None:
            if currentNode.data == n:
                count += 1
            currentNode = currentNode.next
        print("The current count for number", n, "is: ", count)
        return count

    def get(self, index):
        currentNode = self.head
        count = 0
        while currentNode != None:
            if count == index:
                print("The value at index", index, "is: ",currentNode.data)
            count += 1
            currentNode = currentNode.next
        return

    def remove(self, index):
        currentNode = self.head
        previous_node = None
        count = 0
        while currentNode != None:
            if count == index:
                if previous_node != None:
                    previous_node.next = currentNode.next
                else:
                    self.head = currentNode.next
                    return
            previous_node = currentNode
            currentNode = currentNode.next
            count += 1
            print("Removed item check", index)
        return


    
list = LinkedList()
list.head = Node(0)
list.append(1)
list.append(2)
list.append(10)
list.append(None)
list.append(3)
list.append(1)

list.count(1)

list.get(1)
list.get(4)
list.get(5)

list.remove(5)

list.get(5)

