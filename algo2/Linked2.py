class Node:

    def __init__(self, v):
        self.value = v
        self.prev = None
        self.next = None


class LinkedList2:

    def __init__(self):
        self.head = None
        self.tail = None

    def add_in_tail(self, item):
        if self.head is None:
            self.head = item
            item.prev = None
            item.next = None
        else:
            self.tail.next = item
            item.prev = self.tail
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
        while node is not None:
            if node.value == val:
                if node == self.head:
                    self.head = self.head.next
                    if self.head is not None:
                        self.head.prev = None
                elif node == self.tail:
                    self.tail = self.tail.prev
                    if self.tail is not None:
                        self.tail.next = None
                else:
                    node.prev.next = node.next
                    node.next.prev = node.prev

                if not all:
                    break

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
            if not self.head:
                self.head = newNode
                self.head.prev = None
                self.head.next = None
                self.tail = newNode
            else:
                self.add_in_tail(newNode)
        else:
            while node is not None:
                if node == afterNode:
                    newNode.prev = afterNode
                    newNode.next = afterNode.next
                    if newNode.next is None:
                        self.tail = newNode
                    else:
                        newNode.next.prev = newNode
                    newNode.prev.next = newNode
                node = node.next

    def add_in_head(self, newNode):
        node = self.head
        node.prev = newNode
        newNode.next = node
        self.head = newNode
