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

        self.node_11 = SimpleTreeNode(11, None)
        self.tree3 = SimpleTree(SimpleTreeNode(1, None))

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

    def test_get_all_nodes2(self):
        temp_tree = SimpleTree()
        self.assertEqual(temp_tree.GetAllNodes(), [])

    def test_delete_child(self):
        self.tree2.DeleteNode(self.node_to_delete2)
        nodes = self.tree2.GetAllNodes()
        values = []
        for node in nodes:
            values.append(node.NodeValue)
        self.assertEqual(values, [11, 15])

    def test_delete_child2(self):
        self.tree2.DeleteNode(self.root_node2)
        self.assertEqual(self.tree2.Root, None)

    def test_find_by_value(self):
        self.assertEqual(self.tree2.FindNodesByValue(11), [self.root_node2])
        self.tree2.AddChild(self.node_to_delete2, self.node_11)
        self.assertEqual(self.tree2.FindNodesByValue(11), [self.root_node2, self.node_11])

    def test_move_node(self):
        self.tree2.AddChild(self.root_node2, self.node_11)
        nodes = self.tree2.GetAllNodes()
        values = []
        for node in nodes:
            values.append(node.NodeValue)
        self.assertEqual(values, [11, 13, 17, 15, 11])
        self.tree2.MoveNode(self.node_11, self.node_to_delete2)
        nodes = self.tree2.GetAllNodes()
        values = []
        for node in nodes:
            values.append(node.NodeValue)
        self.assertEqual(values, [11, 13, 17, 11, 15])

    def test_count(self):
        self.assertEqual(self.tree2.Count(), 4)
        self.tree2.AddChild(self.root_node2, self.node_11)
        self.assertEqual(self.tree2.Count(), 5)

    def test_leaf_count(self):
        self.assertEqual(self.tree2.LeafCount(), 2)
        self.tree2.AddChild(self.root_node2, self.node_11)
        self.assertEqual(self.tree2.LeafCount(), 3)


unittest.main()
