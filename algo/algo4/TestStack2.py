import unittest
from Stack2 import Stack

class TestStack(unittest.TestCase):
    def setUp(self):
        self.stack1 = Stack()
        self.stack1.push(1)
        self.stack1.push(2)
        self.stack1.push(3)

    def testStack1(self):
        self.stack1.push(4)
        self.assertEqual(self.stack1.size(), 4)
        self.assertEqual(self.stack1.pop(), 4)
        self.assertEqual(self.stack1.size(), 3)
        self.assertEqual(self.stack1.pop(), 3)
        self.assertEqual(self.stack1.size(), 2)
        self.assertEqual(self.stack1.pop(), 2)
        self.assertEqual(self.stack1.size(), 1)
        self.assertEqual(self.stack1.pop(), 1)
        self.assertEqual(self.stack1.size(), 0)
        self.assertEqual(self.stack1.pop(), None)

    def testStack2(self):
        self.assertEqual(self.stack1.size(), 3)
        self.assertEqual(self.stack1.peek(), 3)
        self.assertEqual(self.stack1.size(), 3)

unittest.main()