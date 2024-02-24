import unittest
from LinkedList import LinkedList
from TwoWayList import TwoWayList


class TestLists(unittest.TestCase):

    def setUp(self) -> None:
        self.list1 = LinkedList()
        self.list2 = TwoWayList()

    def test_creation(self):
        self.assertEqual(self.list1.get_head_status(), LinkedList.HEAD_NIL)
        self.assertEqual(self.list2.get_head_status(), TwoWayList.HEAD_NIL)

    def test_add_to_tail(self):
        self.list1.add_tail(5)
        self.list2.add_tail(6)
        self.assertEqual(self.list1.get_head_status(), LinkedList.HEAD_OK)
        self.assertEqual(self.list2.get_head_status(), TwoWayList.HEAD_OK)

unittest.main()
