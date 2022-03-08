import unittest
from BST import BSTNode, BSTFind, BST


class TestSimpleTree(unittest.TestCase):
    def setUp(self):
        self.root1 = BSTNode(11, 11, None)
        self.bst1 = BST(self.root1)

        self.root2 = BSTNode(11, 11, None)
        self.bst2 = BST(self.root2)
        self.bst2.AddKeyValue(9, 9)
        self.bst2.AddKeyValue(15, 15)
        self.bst2.AddKeyValue(13, 13)
        self.bst2.AddKeyValue(17, 17)

    def test_add_key_value(self):
        self.assertEqual(self.root1.LeftChild, None)
        self.assertTrue(self.bst1.AddKeyValue(9, 9))
        self.assertEqual(self.root1.LeftChild.NodeValue, 9)
        self.assertEqual(self.root1.RightChild, None)
        self.assertTrue(self.bst1.AddKeyValue(15, 15))
        self.assertEqual(self.root1.RightChild.NodeValue, 15)
        self.assertTrue(self.bst1.AddKeyValue(13, 13))
        self.assertTrue(self.bst1.AddKeyValue(17, 17))
        self.assertTrue(self.bst1.AddKeyValue(12, 12))
        self.assertFalse(self.bst1.AddKeyValue(9, 9))

    def test_find_node_by_key(self):
        bst_res1 = self.bst2.FindNodeByKey(12)
        self.assertEqual(bst_res1.Node.NodeValue, 13)
        self.assertFalse(bst_res1.NodeHasKey)
        self.assertTrue(bst_res1.ToLeft)
        bst_res2 = self.bst2.FindNodeByKey(14)
        self.assertEqual(bst_res2.Node.NodeValue, 13)
        self.assertFalse(bst_res2.NodeHasKey)
        self.assertFalse(bst_res2.ToLeft)
        bst_res3 = self.bst2.FindNodeByKey(13)
        self.assertEqual(bst_res3.Node.NodeValue, 13)
        self.assertTrue(bst_res3.NodeHasKey)

unittest.main()
