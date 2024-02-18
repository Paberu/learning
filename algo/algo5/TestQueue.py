import unittest
from Queue import Queue

class TestStack(unittest.TestCase):
    def setUp(self):
        self.queue1 = Queue()
        self.queue2 = Queue()
        self.queue2.enqueue(1)
        self.queue2.enqueue(2)
        self.queue2.enqueue(3)
        self.queue2.enqueue(4)

    def testQueue1(self):
        self.queue1.enqueue(1)
        self.assertEqual(self.queue1.size(), 1)
        self.queue1.enqueue(2)
        self.assertEqual(self.queue1.size(), 2)
        self.queue1.enqueue(3)
        self.assertEqual(self.queue1.size(), 3)
        self.queue1.enqueue(4)
        self.assertEqual(self.queue1.size(), 4)
        self.assertEqual(self.queue1.dequeue(), 1)
        self.assertEqual(self.queue1.size(), 3)
        self.assertEqual(self.queue1.dequeue(), 2)
        self.assertEqual(self.queue1.size(), 2)
        self.assertEqual(self.queue1.dequeue(), 3)
        self.assertEqual(self.queue1.size(), 1)
        self.assertEqual(self.queue1.dequeue(), 4)
        self.assertEqual(self.queue1.size(), 0)
        self.assertEqual(self.queue1.dequeue(), None)

    def testQueue2(self):
        self.rotate(self.queue2, 1)
        self.assertEqual(self.queue2.view(), [2,3,4,1])
        self.rotate(self.queue2, 2)
        self.assertEqual(self.queue2.view(), [4,1,2,3])

    def rotate(self, q, n):
        for _ in range(n):
            q.enqueue(q.dequeue())


unittest.main()