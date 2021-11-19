class Node:

    def __init__(self, v):
        self.value = v
        self.next = None


class LinkedList:

    def __init__(self):
        self.head = None
        self.tail = None

    def add_in_tail(self, item):
        if self.head is None:
            self.head = item
        else:
            self.tail.next = item
        self.tail = item

    def print_all_nodes(self):
        node = self.head
        while node is not None:
            print(node.value)
            node = node.next

    def find(self, val):
        node = self.head
        while node is not None:
            if node.value == val:
                return node
            node = node.next
        return None

    def find_all(self, val):
        node = self.head
        result = []
        while node is not None:
            if node.value == val:
                result.append(node)
            node = node.next
        return result

    def delete(self, val, all=False):
        node = self.head
        previous = self.head
        while node is not None:
            if node.value == val:
                if node == self.head:
                    self.head = node.next
                elif node == self.tail:
                    previous.next = None
                    self.tail = previous
                else:
                    previous.next = node.next

                if not all:
                    break
                else:
                    node = node.next
            else:
                previous = node
                node = node.next

        if self.head is None:
            self.tail = None

    def clean(self):
        self.head = None
        self.tail = None

    def len(self):
        node = self.head
        length = 0
        while node is not None:
            length += 1
            node = node.next
        return length

    def insert(self, afterNode, newNode):
        node = self.head
        if not afterNode:
            self.head = newNode
            newNode.next = node
            if node is None:
                self.tail = newNode
        else:
            while node is not None:
                if node == afterNode:
                    newNode.next = node.next
                    node.next = newNode
                    if newNode.next is None:
                        self.tail = newNode
                node = node.next

    def compare_to_another_list(self, anotherList):
        resultList = LinkedList()
        if self.len() == anotherList.len():
            node = self.head
            anotherNode = anotherList.head
            while node is not None:
                new_node = Node(node.value + anotherNode.value)
                resultList.add_in_tail(new_node)
                node = node.next
                anotherNode = anotherNode.next
        return resultList
