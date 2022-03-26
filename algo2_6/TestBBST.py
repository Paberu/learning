import unittest
from BalancedBST import BalancedBST, BSTNode


class TestSimpleTree(unittest.TestCase):

    def test_one_node(self):
        bbst = BalancedBST()
        bbst.GenerateTree([5])
        self.assertTrue(bbst.Root.NodeKey, 5)
        self.assertTrue(bbst.IsBalanced(bbst.Root))

    def test_two_node(self):
        bbst = BalancedBST()
        bbst.GenerateTree([5, 8])
        self.assertEqual(bbst.Root.NodeKey, 5)
        self.assertEqual(bbst.Root.RightChild.NodeKey, 8)
        self.assertEqual(bbst.Root.LeftChild, None)
        self.assertTrue(bbst.IsBalanced(bbst.Root))

    def test_three_node(self):
        bbst = BalancedBST()
        bbst.GenerateTree([9, 5, 7])
        self.assertEqual(bbst.Root.NodeKey, 7)
        self.assertEqual(bbst.Root.RightChild.NodeKey, 9)
        self.assertEqual(bbst.Root.LeftChild.NodeKey, 5)
        self.assertTrue(bbst.IsBalanced(bbst.Root))

    def test_generation(self):
        a = [9, 8, 7, 6, 10, 1, 2, 3, 4, 5, 0]
        bbst = BalancedBST()
        bbst.GenerateTree(a)
        self.assertTrue(bbst.IsBalanced(bbst.Root))


unittest.main()
