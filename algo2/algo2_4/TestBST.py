import unittest
from BST import aBST


class TestSimpleTree(unittest.TestCase):
    def setUp(self):
        self.bst1 = aBST(2)
        self.bst2 = aBST(1)
        self.bst2.Tree = [5, 3, 7]

    def test_find_key(self):
        self.assertEqual(self.bst2.FindKeyIndex(5), 0)
        self.assertEqual(self.bst2.FindKeyIndex(3), 1)
        self.assertEqual(self.bst2.FindKeyIndex(7), 2)

    def test_add_key(self):
        self.assertEqual(self.bst1.AddKey(5), 0)
        self.assertEqual(self.bst1.AddKey(3), 1)
        self.assertEqual(self.bst1.AddKey(7), 2)
        self.assertEqual(self.bst1.AddKey(5), 0)

    def test_array(self):
        bst = aBST(3)
        self.assertEqual(bst.AddKey(11), 0)
        self.assertEqual(bst.AddKey(9), 1)
        self.assertEqual(bst.AddKey(15), 2)
        self.assertEqual(bst.AddKey(7), 3)
        self.assertEqual(bst.AddKey(10), 4)
        self.assertEqual(bst.AddKey(13), 5)
        self.assertEqual(bst.AddKey(17), 6)
        self.assertEqual(bst.AddKey(5), 7)
        self.assertEqual(bst.AddKey(14), 12)
        self.assertEqual(bst.Tree, [11, 9, 15, 7, 10, 13, 17, 5, None, None, None, None, 14, None, None])


unittest.main()
