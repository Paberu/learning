import unittest

from Queue import Queue
from Queue2 import Queue2


class TestQueue(unittest.TestCase):

    def setUp(self):
        self.queue1 = Queue()
        self.queue2 = Queue2()

    def testEnqueue1(self):
        self.queue1._enqueue(0)
        self.assertEqual(self.queue1.get_head_status(), Queue.HEAD_OK)
        self.queue1._enqueue(10)
        self.assertEqual(len(self.queue1), 2)

    def testEnqueue2(self):
        self.queue2._enqueue(0)
        self.assertEqual(self.queue2.get_head_status(), Queue2.HEAD_OK)
        self.queue2._enqueue(10)
        self.assertEqual(len(self.queue2), 2)

    def testDequeue1(self):
        self.queue1._enqueue(0)
        self.queue1._enqueue(10)
        self.assertEqual(self.queue1._dequeue(), 0)
        self.assertEqual(self.queue1.get_dequeue_status(), Queue.DEQUEUE_OK)
        self.assertEqual(self.queue1._dequeue(), 10)
        self.assertEqual(self.queue1.get_dequeue_status(), Queue.DEQUEUE_OK)
        self.assertEqual(self.queue1._dequeue(), 0)
        self.assertEqual(self.queue1.get_dequeue_status(), Queue.DEQUEUE_ERR)

    def testDequeue2(self):
        self.queue2._enqueue(0)
        self.queue2._enqueue(10)
        self.assertEqual(self.queue2._dequeue(), 0)
        self.assertEqual(self.queue2.get_dequeue_status(), Queue.DEQUEUE_OK)
        self.assertEqual(self.queue2._dequeue(), 10)
        self.assertEqual(self.queue2.get_dequeue_status(), Queue.DEQUEUE_OK)
        self.assertEqual(self.queue2._dequeue(), 0)
        self.assertEqual(self.queue2.get_dequeue_status(), Queue.DEQUEUE_ERR)


unittest.main()
