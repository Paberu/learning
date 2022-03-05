import unittest
from SimpleTree import SimpleTreeNode, SimpleTree


class TestSimpleTree(unittest.TestCase):
    def setUp(self):
        self.root_node = SimpleTreeNode(12)
        self.tree1 = SimpleTree(self.root_node)

        self.root_node2 = SimpleTreeNode(11)
        self.tree2 = SimpleTree(self.root_node2)
        self.node_to_delete2 = SimpleTreeNode(13, self.root_node2)
        self.tree2.AddChild(self.root_node2, SimpleTreeNode(15))
        self.tree2.AddChild(self.node_to_delete2, SimpleTreeNode(17))

        self.node_11 = SimpleTreeNode(11)
        self.tree3 = SimpleTree(SimpleTreeNode(1))

    def test_add_child(self):
        self.tree1.AddChild(self.tree1.Root, SimpleTreeNode(9))
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

    def test_get_all_nodes3(self):
        tmp_node = SimpleTreeNode(42)
        self.tree1.AddChild(self.root_node, tmp_node)
        nodes = self.tree1.GetAllNodes()
        self.assertEqual(len(nodes), 2)
        values = []
        for node in nodes:
            values.append(node.NodeValue)
        self.assertEqual(values, [12, 42])

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

    def test_two_node_tree(self):
        tree = SimpleTree(SimpleTreeNode(1))
        self.assertEqual(tree.Count(), 1)
        self.assertEqual(tree.LeafCount(), 1)
        tree.AddChild(tree.Root, SimpleTreeNode(2))
        self.assertEqual(tree.Count(), 2)
        self.assertEqual(tree.LeafCount(), 1)        


unittest.main()
