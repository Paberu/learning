import unittest
from SimpleTree import SimpleTree, SimpleTreeNode


class TestSimpleTree(unittest.TestCase):

    def test_simplest_tree(self):
        tree1 = SimpleTree(SimpleTreeNode(1, None))
        tree1.AddChild(tree1.Root, SimpleTreeNode(2, tree1.Root))
        tree1.AddChild(tree1.Root, SimpleTreeNode(5, tree1.Root))
        self.assertEqual(tree1.EvenTrees(), [])

    def test_simple_tree(self):
        tree2 = SimpleTree(SimpleTreeNode(1, None))
        node2 = SimpleTreeNode(2, tree2.Root)
        node3 = SimpleTreeNode(3, tree2.Root)
        node6 = SimpleTreeNode(6, tree2.Root)
        tree2.AddChild(tree2.Root, node2)
        tree2.AddChild(tree2.Root, node3)
        tree2.AddChild(tree2.Root, node6)
        tree2.AddChild(node2, SimpleTreeNode(5, node2))
        tree2.AddChild(node2, SimpleTreeNode(7, node2))
        tree2.AddChild(node3, SimpleTreeNode(4, node2))
        node8 = SimpleTreeNode(8, node6)
        tree2.AddChild(node6, node8)
        tree2.AddChild(node8, SimpleTreeNode(9, node8))
        tree2.AddChild(node8, SimpleTreeNode(10, node8))
        self.assertEqual(tree2.EvenTrees(), [1, 3, 1, 6])


unittest.main()
