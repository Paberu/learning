import unittest

from BoundedStack import BoundedStack


class TestBoundedStack(unittest.TestCase):
    def setUp(self) -> None:
        self.stack1 = BoundedStack()
        self.stack2 = BoundedStack(size=4)

    def testNilStatuses(self):
        self.assertEqual(self.stack1.get_pop_status(), BoundedStack.POP_NIL)
        self.assertEqual(self.stack1.get_peek_status(), BoundedStack.PEEK_NIL)
        self.assertEqual(self.stack1.get_push_status(), BoundedStack.PUSH_NIL)

    def testPush(self):
        for i in range(4):
            self.stack2.push(i)
        self.assertEqual(self.stack2.size(), 4)
        self.assertEqual(self.stack2.get_push_status(), BoundedStack.PUSH_OK)
        self.stack2.push(4)
        self.assertEqual(self.stack2.size(), 4)
        self.assertEqual(self.stack2.get_push_status(), BoundedStack.PUSH_ERR)

    def testPop(self):
        self.stack1.push(0)
        self.stack1.pop()
        self.assertEqual(self.stack1.get_pop_status(), BoundedStack.POP_OK)
        self.stack1.pop()
        self.assertEqual(self.stack1.get_pop_status(), BoundedStack.POP_ERR)
        self.assertEqual(self.stack1.size(), 0)


unittest.main()
