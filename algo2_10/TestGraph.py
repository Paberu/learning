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
        v_from = self.graph.vertex[0]
        v_to = self.graph.vertex[1]
        values = [vert.Value for vert in self.graph.DepthFirstSearch(v_from, v_to)]
        self.assertTrue(values, [1, 0])

    def test_depth_first_search02(self):
        v_from = self.graph.vertex[0]
        v_to = self.graph.vertex[2]
        values = [vert.Value for vert in self.graph.DepthFirstSearch(v_from, v_to)]
        self.assertTrue(values, [2, 0])

    def test_depth_first_search03(self):
        v_from = self.graph.vertex[0]
        v_to = self.graph.vertex[3]
        values = [vert.Value for vert in self.graph.DepthFirstSearch(v_from, v_to)]
        self.assertTrue(values, [3, 1, 0])

    def test_depth_first_search06(self):
        v_from = self.graph.vertex[0]
        v_to = self.graph.vertex[6]
        values = [vert.Value for vert in self.graph.DepthFirstSearch(v_from, v_to)]
        self.assertTrue(values, [6, 2, 0])

    def test_depth_first_search59(self):
        v_from = self.graph.vertex[5]
        v_to = self.graph.vertex[9]
        values = [vert.Value for vert in self.graph.DepthFirstSearch(v_from, v_to)]
        self.assertTrue(values, [5, 2, 0, 1, 4, 8, 9])


unittest.main()
