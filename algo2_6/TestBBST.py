import unittest
from BalancedBST import BalancedBST, BSTNode


class TestSimpleTree(unittest.TestCase):
    def test_generation(self):
        a = [9, 8, 7, 6, 10, 1, 2, 3, 4, 5, 0]
        bbst = BalancedBST()
        bbst.GenerateTree(a)
        self.assertEqual(bbst.get_root(), [5, 2, 8])
        self.assertTrue(bbst.IsBalanced(bbst.Root))


unittest.main()
