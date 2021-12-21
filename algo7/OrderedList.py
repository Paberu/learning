class Node:
    def __init__(self, v):
        self.value = v
        self.prev = None
        self.next = None

class OrderedList:
    def __init__(self, asc):
        self.head = None
        self.tail = None
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
        if self.head is None:
            self.head = self.tail = node
        else:
            asc = 1 if self.__ascending else -1
            if self.compare(value, self.head.value) in (0, -asc):
                self.head.prev = node
                node.next = self.head
                self.head = node
            elif self.compare(value, self.tail.value) in (0, asc):
                self.tail.next = node
                node.prev = self.tail
                self.tail = node
            else:
                left = self.head
                right = self.tail
                while self.compare(left.next.value, value) in (0, -asc) and self.compare(right.prev.value, value) in (0, asc):
                    left = left.next
                    right = right.prev
                if self.compare(left.next.value, value) in (0, asc):
                    node.next = left.next
                    node.prev = left
                elif self.compare(right.prev.value, value) in (0, -asc):
                    node.prev = right.prev
                    node.next = right
                node.next.prev = node
                node.prev.next = node
        self.size += 1

    def find(self, val):
        asc = 1 if self.__ascending else -1
        if self.compare(val, self.head.value) == -asc or self.compare(val, self.tail.value) == asc:
            return None
        else:
            node = self.head
            while node is not None:
                if self.compare(val, node.value) == asc:
                    node = node.next
                elif self.compare(val, node.value) == 0:
                    return node
                else:
                    return None
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
                self.size -= 1
                break
            else:
                node = node.next
        if self.head is None:
            self.tail = None

    def clean(self, asc):
        self.__ascending = asc
        self.head = self.tail = None
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
        if v1.split() < v2.split():
            return -1
        elif v1.split > v2.split():
            return 1
        return 0