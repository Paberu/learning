class Stack:
    def __init__(self):
        self.head = None
        self.tail = None
        self.depth = 0

    def size(self):
        return self.depth

    def pop(self):
        item = self.head
        if item:
            if self.depth == 1:
                self.__init__()
            else:
                self.head = self.head.next
                self.head.prev = None
                self.depth -= 1
            return item.value
        return None

    def push(self, value):
        item = self.Node(value)
        if self.head is None:
            self.head = self.tail = item
        else:
            self.head.prev = item
            item.next = self.head
            self.head = item
        self.depth += 1

    def peek(self):
        if self.head:
            return self.head.value
        return None

    class Node:

        def __init__(self, v):
            self.value = v
            self.prev = None
            self.next = None