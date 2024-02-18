class Deque:
    def __init__(self):
        self.head = None
        self.tail = None
        self.depth = 0

    def addFront(self, item):
        node = self.Node(item)
        if self.head is None:
            self.head = self.tail = node
        else:
            self.head.prev = node
            node.next = self.head
            self.head = node
        self.depth += 1

    def addTail(self, item):
        node = self.Node(item)
        if self.head is None:
            self.head = self.tail = node
        else:
            self.tail.next = node
            node.prev = self.tail
            self.tail = node
        self.depth += 1

    def removeFront(self):
        node = self.head
        if node:
            if self.depth == 1:
                self.__init__()
            else:
                self.head = self.head.next
                self.head.prev = None
                self.depth -= 1
            return node.value
        return None

    def removeTail(self):
        node = self.tail
        if node:
            if  self.depth == 1:
                self.__init__()
            else:
                self.tail = self.tail.prev
                self.tail.next = None
                self.depth -= 1
            return node.value
        return None

    def peek_front(self):
        if self.head:
            return self.head.value
        return None

    def peek_tail(self):
        if self.tail:
            return self.tail.value
        return None

    def size(self):
        return self.depth

    class Node:

        def __init__(self, v):
            self.value = v
            self.prev = None
            self.next = None
