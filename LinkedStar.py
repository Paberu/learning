from Linked import Node, LinkedList
import unittest

class TestLinkedList(unittest.TestCase):
    
    def setUp(self):
        self.list1 = LinkedList()
        self.list1.add_in_tail(Node(12))
        self.list1.add_in_tail(Node(55))
        self.list1.add_in_tail(Node(128))
        self.list1.add_in_tail(Node(12))
        self.list1.add_in_tail(Node(56))
        self.list1.add_in_tail(Node(128))

        self.list2 = LinkedList()

        self.list3 = LinkedList()
        self.list3.add_in_tail(Node(11))
        self.list3.add_in_tail(Node(55))
        self.list3.add_in_tail(Node(1))
        self.list3.add_in_tail(Node(11))
        self.list3.add_in_tail(Node(56))
        self.list3.add_in_tail(Node(1))

        self.list4 = LinkedList()

    def tearDown(self):
                result = self.defaultTestResult()

    def test_find_all(self):
        self.assertEqual(self.list1.find_all(12), [12, 12])
        self.assertEqual(self.list1.find_all(55), [55])
        self.assertEqual(self.list1.find_all(2), [])
        
        self.assertEqual(self.list2.find_all(12), [])
        
    def test_delete(self):
        self.list1.delete(9)
        self.assertEqual(get_list_values(self.list1), [12, 55, 128, 12, 56, 128])
        self.list1.delete(12)
        self.assertEqual(get_list_values(self.list1), [55, 128, 12, 56, 128])
        self.list1.delete(128, all=True)
        self.assertEqual(get_list_values(self.list1), [55, 12, 56])
        
        self.list2.delete(12, all=True)
        self.assertEqual(get_list_values(self.list2), [])
    
    def test_clean(self):
        self.list1.clean()
        self.assertEqual(self.list1.head, None)
        self.assertEqual(self.list1.tail, None)
        
        self.list2.clean()
        self.assertEqual(self.list2.head, None)
        self.assertEqual(self.list2.tail, None)
    
    def test_len(self):
        self.assertEqual(self.list1.len(), 6)
        self.assertEqual(self.list2.len(), 0)
        
    # def test_compare(self):
    #   self.assertEqual()
        
def get_list_values(list_to_values):
    values = []
    node = list_to_values.head
    while node is not None:
        values.append(node.value)
        node = node.next
    return values


tester = TestLinkedList()
##tester.main()
##tester.setUp()
##tester.test_len()
##
##tester.setUp()
##tester.test_clean()
##
##tester.setUp()
##tester.test_delete()
