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

        self.root3 = BSTNode(11, 11, None)
        self.bst3 = BST(self.root3)
        self.bst3.AddKeyValue(9, 9)
        self.bst3.AddKeyValue(15, 15)
        self.bst3.AddKeyValue(13, 13)
        self.bst3.AddKeyValue(17, 17)
        self.bst3.AddKeyValue(7, 7)
        self.bst3.AddKeyValue(10, 10)
        self.bst3.AddKeyValue(5, 5)
        self.bst3.AddKeyValue(9.5, 9.5)
        self.bst3.AddKeyValue(10.5, 10.5)
        self.bst3.AddKeyValue(14, 14)
        self.bst3.AddKeyValue(19, 19)

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

    def test_count(self):
        self.assertEqual(self.bst2.Count(), 5)

    def test_wide_all_nodes(self):
        # for each in self.bst3.WideAllNodes():
        #     print(each.NodeValue)
        pass

    def test_deep_all_nodes(self):
        for each in self.bst3.DeepAllNodes(3):
            print(each.NodeValue)

unittest.main()
