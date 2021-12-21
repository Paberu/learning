import unittest

from OrderedList import OrderedList

class TestOrderedList(unittest.TestCase):
    def setUp(self):
        self.ol1 = OrderedList(True)
        self.ol1.add(1)
        self.ol1.add(2)
        self.ol1.add(3)
        self.ol1.add(4)
        self.ol1.add(5)
        self.ol1.add(6)
        self.ol1.add(7)
        self.ol1.add(8)
        self.ol1.add(9)
        self.ol1.add(10)
        self.ol2 = OrderedList(True)
        self.ol3 = OrderedList(False)
        self.ol4 = OrderedList(False)
        self.ol4.add(1)
        self.ol4.add(2)
        self.ol4.add(3)
        self.ol4.add(4)
        self.ol4.add(5)
        self.ol4.add(6)
        self.ol4.add(7)
        self.ol4.add(8)
        self.ol4.add(9)
        self.ol4.add(10)

    def test_add1(self):
        self.ol2.add(2)
        self.assertEqual(self.ol2.head.value, 2)
        self.assertEqual(self.ol2.tail.value, 2)
        self.assertEqual(self.ol2.len(), 1)
        self.ol2.add(5)
        self.assertEqual(self.ol2.head.value, 2)
        self.assertEqual(self.ol2.head.next.value, 5)
        self.assertEqual(self.ol2.tail.prev.value, 2)
        self.assertEqual(self.ol2.tail.value, 5)
        self.assertEqual(self.ol2.len(), 2)
        self.ol2.add(8)
        self.assertEqual(self.ol2.head.value, 2)
        self.assertEqual(self.ol2.head.next.value, 5)
        self.assertEqual(self.ol2.tail.prev.value, 5)
        self.assertEqual(self.ol2.tail.value, 8)
        self.assertEqual(self.ol2.len(), 3)
        self.ol2.add(3)
        self.assertEqual(self.ol2.head.value, 2)
        self.assertEqual(self.ol2.head.next.value, 3)
        self.assertEqual(self.ol2.tail.prev.value, 5)
        self.assertEqual(self.ol2.tail.value, 8)
        self.assertEqual(self.ol2.len(), 4)
        self.ol2.add(4)
        self.assertEqual(self.ol2.head.value, 2)
        self.assertEqual(self.ol2.head.next.value, 3)
        self.assertEqual(self.ol2.tail.prev.value, 5)
        self.assertEqual(self.ol2.tail.value, 8)
        self.assertEqual(self.ol2.len(), 5)
        self.ol2.add(1)
        self.assertEqual(self.ol2.head.value, 1)
        self.assertEqual(self.ol2.head.next.value, 2)
        self.assertEqual(self.ol2.tail.prev.value, 5)
        self.assertEqual(self.ol2.tail.value, 8)
        self.assertEqual(self.ol2.len(), 6)
        self.ol2.add(9)
        self.assertEqual(self.ol2.head.value, 1)
        self.assertEqual(self.ol2.head.next.value, 2)
        self.assertEqual(self.ol2.tail.prev.value, 8)
        self.assertEqual(self.ol2.tail.value, 9)
        self.assertEqual(self.ol2.len(), 7)
        self.ol2.add(6)
        self.assertEqual(self.ol2.head.value, 1)
        self.assertEqual(self.ol2.head.next.value, 2)
        self.assertEqual(self.ol2.tail.prev.value, 8)
        self.assertEqual(self.ol2.tail.value, 9)
        self.assertEqual(self.ol2.len(), 8)
        self.ol2.add(7)
        self.assertEqual(self.ol2.head.value, 1)
        self.assertEqual(self.ol2.head.next.value, 2)
        self.assertEqual(self.ol2.tail.prev.value, 8)
        self.assertEqual(self.ol2.tail.value, 9)
        self.assertEqual(self.ol2.len(), 9)
        self.ol2.add(10)
        self.assertEqual(self.ol2.head.value, 1)
        self.assertEqual(self.ol2.head.next.value, 2)
        self.assertEqual(self.ol2.tail.prev.value, 9)
        self.assertEqual(self.ol2.tail.value, 10)
        self.assertEqual(self.ol2.len(), 10)

    def test_add2(self):
        self.ol3.add(2)
        self.assertEqual(self.ol3.head.value, 2)
        self.assertEqual(self.ol3.tail.value, 2)
        self.assertEqual(self.ol3.len(), 1)
        self.ol3.add(5)
        self.assertEqual(self.ol3.head.value, 5)
        self.assertEqual(self.ol3.head.next.value, 2)
        self.assertEqual(self.ol3.tail.prev.value, 5)
        self.assertEqual(self.ol3.tail.value, 2)
        self.assertEqual(self.ol3.len(), 2)
        self.ol3.add(8)
        self.assertEqual(self.ol3.head.value, 8)
        self.assertEqual(self.ol3.head.next.value, 5)
        self.assertEqual(self.ol3.tail.prev.value, 5)
        self.assertEqual(self.ol3.tail.value, 2)
        self.assertEqual(self.ol3.len(), 3)
        self.ol3.add(3)
        self.assertEqual(self.ol3.head.value, 8)
        self.assertEqual(self.ol3.head.next.value, 5)
        self.assertEqual(self.ol3.tail.prev.value, 3)
        self.assertEqual(self.ol3.tail.value, 2)
        self.assertEqual(self.ol3.len(), 4)
        self.ol3.add(4)
        self.assertEqual(self.ol3.head.value, 8)
        self.assertEqual(self.ol3.head.next.value, 5)
        self.assertEqual(self.ol3.tail.prev.value, 3)
        self.assertEqual(self.ol3.tail.value, 2)
        self.assertEqual(self.ol3.len(), 5)
        self.ol3.add(1)
        self.assertEqual(self.ol3.head.value, 8)
        self.assertEqual(self.ol3.head.next.value, 5)
        self.assertEqual(self.ol3.tail.prev.value, 2)
        self.assertEqual(self.ol3.tail.value, 1)
        self.assertEqual(self.ol3.len(), 6)
        self.ol3.add(9)
        self.assertEqual(self.ol3.head.value, 9)
        self.assertEqual(self.ol3.head.next.value, 8)
        self.assertEqual(self.ol3.tail.prev.value, 2)
        self.assertEqual(self.ol3.tail.value, 1)
        self.assertEqual(self.ol3.len(), 7)
        self.ol3.add(6)
        self.assertEqual(self.ol3.head.value, 9)
        self.assertEqual(self.ol3.head.next.value, 8)
        self.assertEqual(self.ol3.tail.prev.value, 2)
        self.assertEqual(self.ol3.tail.value, 1)
        self.assertEqual(self.ol3.len(), 8)
        self.ol3.add(7)
        self.assertEqual(self.ol3.head.value, 9)
        self.assertEqual(self.ol3.head.next.value, 8)
        self.assertEqual(self.ol3.tail.prev.value, 2)
        self.assertEqual(self.ol3.tail.value, 1)
        self.assertEqual(self.ol3.len(), 9)
        self.ol3.add(10)
        self.assertEqual(self.ol3.head.value, 10)
        self.assertEqual(self.ol3.head.next.value, 9)
        self.assertEqual(self.ol3.tail.prev.value, 2)
        self.assertEqual(self.ol3.tail.value, 1)
        self.assertEqual(self.ol3.len(), 10)

    def test_find1(self):
        self.assertEqual(self.ol1.find(-1), None)
        self.assertEqual(self.ol1.find(11), None)
        self.assertEqual(self.ol1.find(3).value, 3)
        self.assertEqual(self.ol1.find(3.5), None)

    def test_find2(self):
        self.assertEqual(self.ol4.find(-1), None)
        self.assertEqual(self.ol4.find(11), None)
        self.assertEqual(self.ol4.find(9).value, 9)
        self.assertEqual(self.ol4.find(3.5), None)

    def test_delete1(self):
        self.assertEqual(self.ol1.head.value, 1)
        self.assertEqual(self.ol1.head.next.value, 2)
        self.assertEqual(self.ol1.tail.prev.value, 9)
        self.assertEqual(self.ol1.tail.value, 10)
        self.assertEqual(self.ol1.len(), 10)
        self.ol1.delete(8)
        self.assertEqual(self.ol1.head.value, 1)
        self.assertEqual(self.ol1.head.next.value, 2)
        self.assertEqual(self.ol1.tail.prev.value, 9)
        self.assertEqual(self.ol1.tail.value, 10)
        self.assertEqual(self.ol1.len(), 9)
        self.ol1.delete(6)
        self.assertEqual(self.ol1.head.value, 1)
        self.assertEqual(self.ol1.head.next.value, 2)
        self.assertEqual(self.ol1.tail.prev.value, 9)
        self.assertEqual(self.ol1.tail.value, 10)
        self.assertEqual(self.ol1.len(), 8)
        self.ol1.delete(11)
        self.assertEqual(self.ol1.head.value, 1)
        self.assertEqual(self.ol1.head.next.value, 2)
        self.assertEqual(self.ol1.tail.prev.value, 9)
        self.assertEqual(self.ol1.tail.value, 10)
        self.assertEqual(self.ol1.len(), 8)
        self.ol1.delete(1)
        self.assertEqual(self.ol1.head.value, 2)
        self.assertEqual(self.ol1.head.next.value, 3)
        self.assertEqual(self.ol1.tail.prev.value, 9)
        self.assertEqual(self.ol1.tail.value, 10)
        self.assertEqual(self.ol1.len(), 7)
        self.ol1.delete(10)
        self.assertEqual(self.ol1.head.value, 2)
        self.assertEqual(self.ol1.head.next.value, 3)
        self.assertEqual(self.ol1.tail.prev.value, 7)
        self.assertEqual(self.ol1.tail.value, 9)
        self.assertEqual(self.ol1.len(), 6)
        self.ol1.delete(4)
        self.assertEqual(self.ol1.head.value, 2)
        self.assertEqual(self.ol1.head.next.value, 3)
        self.assertEqual(self.ol1.tail.prev.value, 7)
        self.assertEqual(self.ol1.tail.value, 9)
        self.assertEqual(self.ol1.len(), 5)
        self.ol1.delete(7)
        self.assertEqual(self.ol1.head.value, 2)
        self.assertEqual(self.ol1.head.next.value, 3)
        self.assertEqual(self.ol1.tail.prev.value, 5)
        self.assertEqual(self.ol1.tail.value, 9)
        self.assertEqual(self.ol1.len(), 4)
        self.ol1.delete(5)
        self.assertEqual(self.ol1.head.value, 2)
        self.assertEqual(self.ol1.head.next.value, 3)
        self.assertEqual(self.ol1.tail.prev.value, 3)
        self.assertEqual(self.ol1.tail.value, 9)
        self.assertEqual(self.ol1.len(), 3)
        self.ol1.delete(2)
        self.assertEqual(self.ol1.head.value, 3)
        self.assertEqual(self.ol1.head.next.value, 9)
        self.assertEqual(self.ol1.tail.prev.value, 3)
        self.assertEqual(self.ol1.tail.value, 9)
        self.assertEqual(self.ol1.len(), 2)
        self.ol1.delete(3)
        self.assertEqual(self.ol1.head.value, 9)
        self.assertEqual(self.ol1.tail.value, 9)
        self.assertEqual(self.ol1.len(), 1)
        self.ol1.delete(9)
        self.assertEqual(self.ol1.head, None)
        self.assertEqual(self.ol1.tail, None)
        self.assertEqual(self.ol1.len(), 0)

    def test_delete2(self):
        self.assertEqual(self.ol4.head.value, 10)
        self.assertEqual(self.ol4.head.next.value, 9)
        self.assertEqual(self.ol4.tail.prev.value, 2)
        self.assertEqual(self.ol4.tail.value, 1)
        self.assertEqual(self.ol4.len(), 10)
        self.ol4.delete(9)
        self.assertEqual(self.ol4.head.value, 10)
        self.assertEqual(self.ol4.head.next.value, 8)
        self.assertEqual(self.ol4.tail.prev.value, 2)
        self.assertEqual(self.ol4.tail.value, 1)
        self.assertEqual(self.ol4.len(), 9)
        self.ol4.delete(2)
        self.assertEqual(self.ol4.head.value, 10)
        self.assertEqual(self.ol4.head.next.value, 8)
        self.assertEqual(self.ol4.tail.prev.value, 3)
        self.assertEqual(self.ol4.tail.value, 1)
        self.assertEqual(self.ol4.len(), 8)
        self.ol4.delete(11)
        self.assertEqual(self.ol4.head.value, 10)
        self.assertEqual(self.ol4.head.next.value, 8)
        self.assertEqual(self.ol4.tail.prev.value, 3)
        self.assertEqual(self.ol4.tail.value, 1)
        self.assertEqual(self.ol4.len(), 8)
        self.ol4.delete(1)
        self.assertEqual(self.ol4.head.value, 10)
        self.assertEqual(self.ol4.head.next.value, 8)
        self.assertEqual(self.ol4.tail.prev.value, 4)
        self.assertEqual(self.ol4.tail.value, 3)
        self.assertEqual(self.ol4.len(), 7)
        self.ol4.delete(10)
        self.assertEqual(self.ol4.head.value, 8)
        self.assertEqual(self.ol4.head.next.value, 7)
        self.assertEqual(self.ol4.tail.prev.value, 4)
        self.assertEqual(self.ol4.tail.value, 3)
        self.assertEqual(self.ol4.len(), 6)
        self.ol4.delete(4)
        self.assertEqual(self.ol4.head.value, 8)
        self.assertEqual(self.ol4.head.next.value, 7)
        self.assertEqual(self.ol4.tail.prev.value, 5)
        self.assertEqual(self.ol4.tail.value, 3)
        self.assertEqual(self.ol4.len(), 5)
        self.ol4.delete(7)
        self.assertEqual(self.ol4.head.value, 8)
        self.assertEqual(self.ol4.head.next.value, 6)
        self.assertEqual(self.ol4.tail.prev.value, 5)
        self.assertEqual(self.ol4.tail.value, 3)
        self.assertEqual(self.ol4.len(), 4)
        self.ol4.delete(5)
        self.assertEqual(self.ol4.head.value, 8)
        self.assertEqual(self.ol4.head.next.value, 6)
        self.assertEqual(self.ol4.tail.prev.value, 6)
        self.assertEqual(self.ol4.tail.value, 3)
        self.assertEqual(self.ol4.len(), 3)
        self.ol4.delete(3)
        self.assertEqual(self.ol4.head.value, 8)
        self.assertEqual(self.ol4.head.next.value, 6)
        self.assertEqual(self.ol4.tail.prev.value, 8)
        self.assertEqual(self.ol4.tail.value, 6)
        self.assertEqual(self.ol4.len(), 2)
        self.ol4.delete(8)
        self.assertEqual(self.ol4.head.value, 6)
        self.assertEqual(self.ol4.tail.value, 6)
        self.assertEqual(self.ol4.len(), 1)
        self.ol4.delete(6)
        self.assertEqual(self.ol4.head, None)
        self.assertEqual(self.ol4.tail, None)
        self.assertEqual(self.ol4.len(), 0)

unittest.main()