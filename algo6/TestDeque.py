import unittest
from Deque import Deque


class TestDeque(unittest.TestCase):

    def setUp(self):
        self.deq1 = Deque()

    def test_fill1(self):  # begin with head
        self.deq1.addFront('1head')
        self.assertEqual(self.deq1.peek_front(), '1head')
        self.assertEqual(self.deq1.peek_tail(), '1head')
        self.assertEqual(self.deq1.size(), 1)
        self.deq1.addTail('1tail')
        self.assertEqual(self.deq1.peek_front(), '1head')
        self.assertEqual(self.deq1.peek_tail(), '1tail')
        self.assertEqual(self.deq1.size(), 2)
        self.deq1.addFront('2head')
        self.assertEqual(self.deq1.peek_front(), '2head')
        self.assertEqual(self.deq1.peek_tail(), '1tail')
        self.assertEqual(self.deq1.size(), 3)
        self.deq1.addTail('2tail')
        self.assertEqual(self.deq1.peek_front(), '2head')
        self.assertEqual(self.deq1.peek_tail(), '2tail')
        self.assertEqual(self.deq1.size(), 4)

    def test_fill2(self):  # begin with tail
        self.deq1.addTail('1tail')
        self.assertEqual(self.deq1.peek_front(), '1tail')
        self.assertEqual(self.deq1.peek_tail(), '1tail')
        self.assertEqual(self.deq1.size(), 1)
        self.deq1.addFront('1head')
        self.assertEqual(self.deq1.peek_front(), '1head')
        self.assertEqual(self.deq1.peek_tail(), '1tail')
        self.assertEqual(self.deq1.size(), 2)
        self.deq1.addTail('2tail')
        self.assertEqual(self.deq1.peek_front(), '1head')
        self.assertEqual(self.deq1.peek_tail(), '2tail')
        self.assertEqual(self.deq1.size(), 3)
        self.deq1.addFront('2head')
        self.assertEqual(self.deq1.peek_front(), '2head')
        self.assertEqual(self.deq1.peek_tail(), '2tail')
        self.assertEqual(self.deq1.size(), 4)

    def test_del1(self):  # begin with head
        self.deq1.addFront('1head')
        self.deq1.addTail('1tail')
        self.deq1.addFront('2head')
        self.deq1.addTail('2tail')
        self.assertEqual(self.deq1.peek_front(), '2head')
        self.assertEqual(self.deq1.peek_tail(), '2tail')
        self.assertEqual(self.deq1.size(), 4)
        self.assertEqual(self.deq1.removeFront(), '2head')
        self.assertEqual(self.deq1.size(), 3)
        self.assertEqual(self.deq1.removeFront(), '1head')
        self.assertEqual(self.deq1.size(), 2)
        self.assertEqual(self.deq1.removeFront(), '1tail')
        self.assertEqual(self.deq1.size(), 1)
        self.assertEqual(self.deq1.removeFront(), '2tail')
        self.assertEqual(self.deq1.size(), 0)
        self.assertEqual(self.deq1.removeTail(), None)

    def test_del2(self):  # begin with tail
        self.deq1.addTail('1tail')
        self.deq1.addFront('1head')
        self.deq1.addTail('2tail')
        self.deq1.addFront('2head')
        self.assertEqual(self.deq1.peek_front(), '2head')
        self.assertEqual(self.deq1.peek_tail(), '2tail')
        self.assertEqual(self.deq1.size(), 4)
        self.assertEqual(self.deq1.removeTail(), '2tail')
        self.assertEqual(self.deq1.size(), 3)
        self.assertEqual(self.deq1.removeTail(), '1tail')
        self.assertEqual(self.deq1.size(), 2)
        self.assertEqual(self.deq1.removeTail(), '1head')
        self.assertEqual(self.deq1.size(), 1)
        self.assertEqual(self.deq1.removeTail(), '2head')
        self.assertEqual(self.deq1.size(), 0)
        self.assertEqual(self.deq1.removeTail(), None)

    def test_check_string1(self):
        self.assertTrue(self.check_string(self.deq1, 'ABBA'))

    def test_check_string2(self):
        self.assertTrue(self.check_string(self.deq1, 'ATMTA'))

    def test_check_string3(self):
        self.assertTrue(self.check_string(self.deq1, 'Murder for a jar of red rum'))

    def test_check_string4(self):
        self.assertFalse(self.check_string(self.deq1, 'Murder for a jar of red rum...'))

    def test_check_string5(self):
        self.assertFalse(self.check_string(self.deq1, 'Not palindrome'))

    def check_string(self, q, string):
        for letter in ''.join(string.split()).lower():
            q.addTail(letter)
        while q.size() > 1:
            if q.removeFront() != q.removeTail():
                return False
        return True

unittest.main()
