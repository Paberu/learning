import unittest
from Graph import SimpleGraph, Vertex


class TestHeap(unittest.TestCase):

    def setUp(self) -> None:
        self.graph = SimpleGraph(5)

    def test_add_vertex(self):
        for i in range(5):
            self.graph.AddVertex(i)
        self.assertEqual([v.Value for v in self.graph.vertex], [0, 1, 2, 3, 4])

    def test_add_vertex2(self):
        for i in range(7):
            self.graph.AddVertex(i)
        self.assertEqual([v.Value for v in self.graph.vertex], [0, 1, 2, 3, 4])

    def test_remove_vertex(self):
        for i in range(5):
            self.graph.AddVertex(i)
        self.graph.RemoveVertex(2)
        test_values = []
        for v in self.graph.vertex:
            if v is not None:
                test_values.append(v.Value)
        self.assertEqual(test_values, [0, 1, 3, 4])

    def test_add_edge(self):
        for i in range(5):
            self.graph.AddVertex(i)
        self.assertTrue(self.graph.AddEdge(3, 3))
        self.assertTrue(self.graph.AddEdge(2, 4))
        self.assertTrue(self.graph.AddEdge(2, 0))
        self.assertTrue(self.graph.IsEdge(3, 3))
        self.assertTrue(self.graph.IsEdge(2, 4))
        self.assertTrue(self.graph.IsEdge(2, 0))

    def test_add_edge3(self):
        graph3 = SimpleGraph(100)
        for i in range(100):
            self.assertTrue(graph3.AddVertex(i))
        for i in range(100):
            for j in range(100):
                self.assertTrue(graph3.AddEdge(i, j))
        for i in range(100):
            for j in range(100):
                self.assertTrue(graph3.IsEdge(i, j))

    def test_is_edge(self):
        for i in range(5):
            self.graph.AddVertex(i)
        self.graph.AddEdge(3, 3)
        self.graph.AddEdge(2, 4)
        self.graph.AddEdge(2, 0)
        self.assertTrue(self.graph.IsEdge(3, 3))
        self.assertFalse(self.graph.IsEdge(2, 3))
        self.assertTrue(self.graph.IsEdge(2, 0))

    def test_remove_edge2(self):
        for i in range(5):
            self.graph.AddVertex(i)
        self.graph.AddEdge(3, 3)
        self.graph.AddEdge(2, 4)
        self.graph.AddEdge(2, 0)
        self.graph.RemoveEdge(2, 4)
        self.assertTrue(self.graph.IsEdge(3, 3))
        self.assertFalse(self.graph.IsEdge(2, 4))
        self.assertTrue(self.graph.IsEdge(2, 0))


unittest.main()