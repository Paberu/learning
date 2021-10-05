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
        while node != None:
            print(node.value)
            node = node.next

    def find(self, val):
        node = self.head
        while node is not None:
            if node.value == val:
                return node
            node = node.next
        return None

    def find_all(self, val): #done
        node = self.head
        result = []
        while node is not None:
            if node.value == val:
                result.append(node)
            node = node.next
        return result

    def delete(self, val, all=False): #done
        node = self.head
        previous = self.head
        while node is not None:
            if node.value == val:
                if node == self.head:
                    self.head = node.next
                else:
                    previous.next = node.next

                if not all:
                    return
            previous = node
            node = node.next

    def clean(self): #done
        self.head = None
        self.tail = None

    def len(self): #done
        node = self.head
        length = 0
        while node is not None:
            length += 1
            node = node.next
        return length

    def insert(self, afterNode, newNode): #done
        node = self.head
        if not afterNode:
            self.head = newNode
            newNode.next = node
        else:
            while node is not None:
                print('trying...')
                if node == afterNode:
                    newNode.next = node.next
                    node.next = newNode
                    return
                node = node.next
                    		

n1 = Node(12)
n2 = Node(55)
n1.next = n2		
s_list = LinkedList()
s_list.add_in_tail(n1)
s_list.add_in_tail(n2)
s_list.add_in_tail(Node(128))
s_list.add_in_tail(Node(12))
s_list.add_in_tail(Node(56))
s_list.add_in_tail(Node(128))
##for n in s_list.find_all(1):
##    print(str(n.value) + ' -> next')
##print(s_list.len())
s_list.print_all_nodes()
print()
##s_list.delete(12,all=True)
n3 = Node(11)
s_list.insert(n2, n3)
##s_list.clean()
s_list.print_all_nodes()
