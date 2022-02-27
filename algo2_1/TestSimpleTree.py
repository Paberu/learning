import unittest
from SimpleTree import SimpleTreeNode, SimpleTree


class TestSimpleTree(unittest.TestCase):
    def setUp(self):
        root_node = SimpleTreeNode(12, None)
        self.tree1 = SimpleTree(root_node)

        self.root_node2 = SimpleTreeNode(11, None)
        self.tree2 = SimpleTree(self.root_node2)
        self.node_to_delete2 = SimpleTreeNode(13, None)
        self.tree2.AddChild(self.root_node2, self.node_to_delete2)
        self.tree2.AddChild(self.root_node2, SimpleTreeNode(15, None))
        self.tree2.AddChild(self.node_to_delete2, SimpleTreeNode(17, None))

    def test_add_child(self):
        self.tree1.AddChild(self.tree1.Root, SimpleTreeNode(9, None))
        self.assertEqual(len(self.tree1.Root.Children), 1)
        self.assertEqual(self.tree1.Root.Children[0].NodeValue, 9)

    def test_get_all_nodes(self):
        nodes = self.tree2.GetAllNodes()
        values = []
        for node in nodes:
            values.append(node.NodeValue)
        self.assertEqual(values, [11, 13, 17, 15])

    def test_delete_child(self):
        self.tree2.DeleteNode(self.node_to_delete2)
        nodes = self.tree2.GetAllNodes()
        values = []
        for node in nodes:
            values.append(node.NodeValue)
        self.assertEqual(values, [11, 15])


unittest.main()