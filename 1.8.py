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
                    		

def compare_and_sum_up(list1, list2):
    if (list1.len() == list2.len()):
        list3 = LinkedList()
        node1 = list1.head
        node2 = list2.head
        while node1 is not None:
            new_node = Node(node1.value + node2.value)
            list3.add_in_tail(new_node)
            node1 = node1.next
            node2 = node2.next
        return list3
	
s_list1 = LinkedList()
s_list1.add_in_tail(Node(5))
s_list1.add_in_tail(Node(15))
s_list1.add_in_tail(Node(12))
s_list2 = LinkedList()
s_list2.add_in_tail(Node(1))
s_list2.add_in_tail(Node(6))
s_list2.add_in_tail(Node(18))
##s_list2.add_in_tail(Node(18))

##s_list1 = LinkedList()
##s_list2 = LinkedList()

s_list3 = compare_and_sum_up(s_list1, s_list2)
if s_list3:
    s_list3.print_all_nodes()

