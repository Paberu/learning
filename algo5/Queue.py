class Queue:
    def __init__(self):
        self.head = None
        self.tail = None
        self.depth = 0

    def enqueue(self, item):
        node = self.Node(item)
        if self.head is None:
            self.head = node
        else:
            self.tail.next = node
            node.prev = self.tail
        self.tail = node
        self.depth += 1

    def dequeue(self):
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

    def size(self):
        return self.depth

    def view(self):
        values = []
        item = self.head
        while item is not None:
            values.append(item.value)
            item = item.next
        return values

    class Node:

        def __init__(self, v):
            self.value = v
            self.prev = None
            self.next = None
