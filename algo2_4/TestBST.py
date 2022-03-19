import unittest
from BST import aBST


class TestSimpleTree(unittest.TestCase):
    def setUp(self):
        self.bst1 = aBST(3)
        self.bst2 = aBST(2)
        self.bst2.Tree = [5, 3, 7]

    def test_find_key(self):
        self.assertEqual(self.bst2.FindKeyIndex(5), 0)
        self.assertEqual(self.bst2.FindKeyIndex(3), 1)
        self.assertEqual(self.bst2.FindKeyIndex(7), 2)


    def test_add_key(self):
        self.assertEqual(self.bst1.AddKey(5), 0)
        self.assertEqual(self.bst1.AddKey(3), 1)
        self.assertEqual(self.bst1.AddKey(7), 2)


unittest.main()
