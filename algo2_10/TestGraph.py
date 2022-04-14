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

    def test_depth_first_search(self):
        v_from = self.graph.vertex[0]
        v_to = self.graph.vertex[9]
        print(self.graph.DepthFirstSearch(v_from, v_to))


unittest.main()
