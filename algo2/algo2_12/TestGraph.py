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

        self.graph2 = SimpleGraph(8)
        for i in range(8):
            self.graph2.AddVertex(i)
        self.graph2.AddEdge(0, 1)
        self.graph2.AddEdge(0, 2)
        self.graph2.AddEdge(0, 3)
        self.graph2.AddEdge(1, 3)
        self.graph2.AddEdge(2, 3)
        self.graph2.AddEdge(1, 4)
        self.graph2.AddEdge(3, 5)
        self.graph2.AddEdge(4, 5)
        self.graph2.AddEdge(5, 6)
        self.graph2.AddEdge(6, 7)

    def test_weak_vertices1(self):
        weaks = self.graph.WeakVertices()
        values = [vert.Value for vert in weaks]
        self.assertEqual(values, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

    def test_weak_vertices2(self):
        weaks = self.graph2.WeakVertices()
        values = [vert.Value for vert in weaks]
        self.assertEqual(values, [4, 5, 6, 7])


unittest.main()
