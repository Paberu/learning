class Node:
    def __init__(self, v):
        self.value = v
        self.prev = None
        self.next = None

class OrderedList:
    def __init__(self, asc):
        self.head = None
        self.tail = None
        self.middle = None
        self.__ascending = asc
        self.size = 0

    def compare(self, v1, v2):
        if v1 < v2:
            return -1
        elif v1 > v2:
            return 1
        return 0

    def add(self, value):
        node = Node(value)
        size += 1
        if size % 2 == 0:
            self.middle = self.middle.next
        if self.head is None:
            self.head = self.tail = self.middle = node
        else:
            if self.__ascending:
                if value <= self.head.value:
                    self.head.prev = node
                    node.next = self.head
                    self.head = node
                elif value >= self.tail.value:
                    self.tail.next = node
                    node.prev = self.tail
                    self.tail = node
                else:
                    left = self.head
                    right = self.tail
                    while left.next.value <= value and right.prev.value >= value:
                        left = left.next
                        right = right.prev
                    if left.next.value > value:
                        node.next = left.next
                        node.prev = left
                    elif right.prev.value < value:
                        node.prev = right.prev
                        node.next = right
                    node.next.prev = node
                    node.prev.next = node
            else:
                if value <= self.tail.value:
                    self.tail.next = node
                    node.prev = self.tail
                    self.tail = node
                elif value >= self.head.value:
                    self.head.prev = node
                    node.next = self.head
                    self.head = node
                else:
                    left = self.head
                    right = self.tail
                    while left.next.value >= value and right.prev.value <= value:
                        left = left.next
                        right = right.prev
                    if left.next.value < value:
                        node.next = left.next
                        node.prev = left
                    elif right.prev.value > value:
                        node.prev = right.prev
                        node.next = right
                    node.next.prev = node
                    node.prev.next = node

    def find(self, val):
        node = self.head
        while node is not None:
            if node.value == val:
                return node
            node = node.next
        return None

    def delete(self, val):
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
                size -= 1
                break
            else:
                node = node.next
        if self.head is None:
            self.tail = None

    def clean(self, asc):
        self.__ascending = asc
        self.head = None
        self.tail = None
        self.size = 0

    def len(self):
        return self.size

    def get_all(self):
        r = []
        node = self.head
        while node != None:
            r.append(node)
            node = node.next
        return r

class OrderedStringList(OrderedList):
    def __init__(self, asc):
        super(OrderedStringList, self).__init__(asc)

    def compare(self, v1, v2):
        if v1 < v2:
            return -1
        elif v1 > v2:
            return 1
        return 0