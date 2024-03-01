import unittest

from Queue import Queue
from Dequeue import Dequeue


class TestQueue(unittest.TestCase):

    def setUp(self):
        self.queue1 = Queue()
        self.queue2 = Dequeue()

    def testEnqueue1(self):
        self.queue1.enqueue(0)
        self.assertEqual(self.queue1.get_head_status(), Queue.HEAD_OK)
        self.queue1.enqueue(10)
        self.assertEqual(len(self.queue1), 2)

    def testEnqueue2(self):
        self.queue2.add_tail(5)
        self.assertEqual(self.queue2.get_head_status(), Dequeue.HEAD_OK)
        self.queue2.add_head(10)
        self.assertEqual(len(self.queue2), 2)

    def testDequeue1(self):
        self.queue1.enqueue(5)
        self.queue1.enqueue(10)
        self.assertEqual(self.queue1.dequeue(), 5)
        self.assertEqual(self.queue1.get_dequeue_status(), Queue.DEQUEUE_OK)
        self.assertEqual(self.queue1.dequeue(), 10)
        self.assertEqual(self.queue1.get_dequeue_status(), Queue.DEQUEUE_OK)
        self.assertEqual(self.queue1.dequeue(), 0)
        self.assertEqual(self.queue1.get_dequeue_status(), Queue.DEQUEUE_ERR)

    def testDequeue2(self):
        self.queue2.add_tail(0)
        self.queue2.add_head(10)
        self.assertEqual(self.queue2.pop_tail(), 0)
        self.assertEqual(self.queue2.get_dequeue_status(), Queue.DEQUEUE_OK)
        self.assertEqual(self.queue2.pop_head(), 10)
        self.assertEqual(self.queue2.get_dequeue_status(), Queue.DEQUEUE_OK)
        self.assertEqual(self.queue2.pop_head(), 0)
        self.assertEqual(self.queue2.get_dequeue_status(), Queue.DEQUEUE_ERR)
        self.assertEqual(self.queue2.pop_tail(), 0)
        self.assertEqual(self.queue2.get_dequeue_status(), Queue.DEQUEUE_ERR)


unittest.main()
