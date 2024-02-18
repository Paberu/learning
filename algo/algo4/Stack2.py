class Stack:
    def __init__(self):
        self.head = None
        self.tail = None
        self.depth = 0

    def size(self):
        return self.depth

    def pop(self):
        item = self.tail
        if item:
            if self.depth == 1:
                self.__init__()
            else:
                self.tail = self.tail.prev
                self.tail.next = None
                self.depth -= 1
            return item.value
        return None

    def push(self, value):
        item = self.Node(value)
        if self.head is None:
            self.head = item
        else:
            self.tail.next = item
            item.prev = self.tail
        self.tail = item
        self.depth += 1

    def peek(self):
        if self.tail:
            return self.tail.value
        return None

    class Node:

        def __init__(self, v):
            self.value = v
            self.prev = None
            self.next = None