class Node:

    def __init__(self, v):
        self.value = v
        self.prev = None
        self.next = None


class DummyNode(Node):

    def __init__(self):
        super().__init__(None)


class LinkedList2:

    def __init__(self):
        self.head = DummyNode()
        self.tail = DummyNode()
        self.tail.prev = self.head
        self.head.next = self.tail
        self.length = 0

    def add_in_tail(self, item):
        item.next = self.tail
        item.prev = self.tail.prev
        self.tail.prev.next = item
        self.tail.prev = item
        self.length += 1

    def print_all_nodes(self):
        node = self.head.next
        while node is not self.tail:
            print(node.value)
            node = node.next

    def find(self, val):
        node = self.head
        while node is not self.tail:
            if node.value == val:
                return node
            node = node.next
        return None

    def find_all(self, val):
        node = self.head
        result = []
        while node is not self.tail:
            if node.value == val:
                result.append(node)
            node = node.next
        return result

    def delete(self, val, all=False):
        node = self.head
        while node is not self.tail:
            if node.value == val:
                node.prev.next = node.next
                node.next.prev = node.prev
                self.length -= 1
                if not all:
                    break
            node = node.next

    def clean(self):
        self.head = DummyNode()
        self.tail = DummyNode()

    def len(self):
        return self.length

    def insert(self, afterNode, newNode):
        if not afterNode:
            self.add_in_tail(newNode)
        else:
            node = self.head.next
            while node is not self.tail:
                if node == afterNode:
                    newNode.prev = afterNode
                    newNode.next = afterNode.next
                    newNode.next.prev = newNode
                    newNode.prev.next = newNode
                    self.length += 1
                    break
                node = node.next

    def add_in_head(self, newNode):
        newNode.next = self.head.next
        newNode.prev = self.head
        self.head.next.prev = newNode
        self.head.next = newNode
        self.length += 1
