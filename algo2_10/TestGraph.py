import unittest
from Graph import SimpleGraph, Vertex


class TestHeap(unittest.TestCase):

    def setUp(self) -> None:
        self.graph = SimpleGraph(11)
        for i in range(11):
            self.graph.AddVertex(i)
        self.graph.AddEdge(0, 1)
        self.graph.AddEdge(0, 2)
        self.graph.AddEdge(1, 3)
        self.graph.AddEdge(1, 4)
        self.graph.AddEdge(2, 5)
        self.graph.AddEdge(2, 6)
        self.graph.AddEdge(4, 7)
        self.graph.AddEdge(4, 8)
        self.graph.AddEdge(8, 9)
        self.graph.AddEdge(8, 10)

    def test_depth_first_search01(self):
        index_from = 0
        index_to = 1
        values = [vert.Value for vert in self.graph.DepthFirstSearch(index_from, index_to)]
        self.assertEqual(values, [0, 1])

    def test_depth_first_search02(self):
        index_from = 0
        index_to = 2
        values = [vert.Value for vert in self.graph.DepthFirstSearch(index_from, index_to)]
        self.assertEqual(values, [0, 2])

    def test_depth_first_search03(self):
        index_from = 0
        index_to = 3
        values = [vert.Value for vert in self.graph.DepthFirstSearch(index_from, index_to)]
        self.assertEqual(values, [0, 1, 3])

    def test_depth_first_search06(self):
        index_from = 0
        index_to = 6
        values = [vert.Value for vert in self.graph.DepthFirstSearch(index_from, index_to)]
        self.assertEqual(values, [0, 2, 6])

    def test_depth_first_search59(self):
        index_from = 5
        index_to = 9
        values = [vert.Value for vert in self.graph.DepthFirstSearch(index_from, index_to)]
        self.assertEqual(values, [5, 2, 0, 1, 4, 8, 9])

    def test_empty_result(self):
        self.graph = SimpleGraph(11)
        for i in range(11):
            self.graph.AddVertex(i)
        self.graph.AddEdge(0, 1)
        self.graph.AddEdge(1, 3)
        self.graph.AddEdge(1, 4)
        self.graph.AddEdge(2, 5)
        self.graph.AddEdge(2, 6)
        self.graph.AddEdge(4, 7)
        self.graph.AddEdge(8, 9)
        self.graph.AddEdge(8, 10)
        values = [vert.Value for vert in self.graph.DepthFirstSearch(2, 8)]
        self.assertEqual(values, [])
        values = [vert.Value for vert in self.graph.DepthFirstSearch(1, 10)]
        self.assertEqual(values, [])


unittest.main()
