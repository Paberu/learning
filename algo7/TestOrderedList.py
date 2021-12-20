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

    def test_add1(self):
        self.ol2.add(2)
        self.assertEqual(self.ol2.head.value, 2)
        self.assertEqual(self.ol2.tail.value, 2)
        self.assertEqual(self.ol2.middle.value, 2)
        self.assertEqual(self.ol2.len(), 1)
        self.ol2.add(5)
        self.assertEqual(self.ol2.head.value, 2)
        self.assertEqual(self.ol2.tail.value, 5)
        self.assertEqual(self.ol2.middle.value, 2)
        self.assertEqual(self.ol2.len(), 2)
        self.ol2.add(8)
        self.assertEqual(self.ol2.head.value, 2)
        self.assertEqual(self.ol2.tail.value, 8)
        self.assertEqual(self.ol2.middle.value,5)
        self.assertEqual(self.ol2.len(), 3)
        self.ol2.add(3)
        self.assertEqual(self.ol2.head.value, 2)
        self.assertEqual(self.ol2.tail.value, 8)
        self.assertEqual(self.ol2.middle.value, 5)
        self.assertEqual(self.ol2.len(), 4)
        self.ol2.add(4)
        self.assertEqual(self.ol2.head.value, 2)
        self.assertEqual(self.ol2.tail.value, 8)
        self.assertEqual(self.ol2.middle.value, 4)
        self.assertEqual(self.ol2.len(), 5)
        self.ol2.add(1)
        self.assertEqual(self.ol2.head.value, 1)
        self.assertEqual(self.ol2.tail.value, 8)
        self.assertEqual(self.ol2.middle.value, 4)
        self.assertEqual(self.ol2.len(), 6)
        self.ol2.add(9)
        self.assertEqual(self.ol2.head.value, 1)
        self.assertEqual(self.ol2.tail.value, 9)
        self.assertEqual(self.ol2.middle.value, 4)
        self.assertEqual(self.ol2.len(), 7)
        self.ol2.add(6)
        self.assertEqual(self.ol2.head.value, 1)
        self.assertEqual(self.ol2.tail.value, 9)
        self.assertEqual(self.ol2.middle.value, 4)
        self.assertEqual(self.ol2.len(), 8)
        self.ol2.add(7)
        self.assertEqual(self.ol2.head.value, 1)
        self.assertEqual(self.ol2.tail.value, 9)
        self.assertEqual(self.ol2.middle.value, 5)
        self.assertEqual(self.ol2.len(), 9)
        self.ol2.add(10)
        self.assertEqual(self.ol2.head.value, 1)
        self.assertEqual(self.ol2.tail.value, 10)
        self.assertEqual(self.ol2.middle.value, 5)
        self.assertEqual(self.ol2.len(), 10)

unittest.main()