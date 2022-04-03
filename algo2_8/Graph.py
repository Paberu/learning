from _operator import index


class Vertex:

    def __init__(self, val):
        self.Value = val


class SimpleGraph:

    def __init__(self, size):
        self.max_vertex = size
        self.m_adjacency = [[0] * size for _ in range(size)]
        self.vertex = [None] * size

    def AddVertex(self, v):
        for i in range(self.max_vertex):
            if self.vertex[i] is None:
                self.vertex = Vertex(v)
                break

    def RemoveVertex(self, v):
        vertex_index = self.max_vertex
        for i in range(self.max_vertex):
            if self.vertex[i].Value == v:
                vertex_index = i
                break
        if vertex_index < self.max_vertex:
            for i in range(self.max_vertex):
                self.m_adjacency[vertex_index][i] = 0
                self.m_adjacency[i][vertex_index] = 0
            self.vertex[vertex_index] = None

    def IsEdge(self, v1, v2):
        v1_index = v2_index = self.max_vertex
        for i in range(self.max_vertex):
            if self.vertex[i].Value == v1:
                v1_index == i
            if self.vertex[i].Value == v2:
                v2_index == i
        if v1_index < self.max_vertex and v2_index<self.max_vertex and\
            (self.m_adjacency[v1_index][v2_index] == 1 or self.m_adjacency[v2_index][v1_index] == 1):
            return True
        # True если есть ребро между вершинами v1 и v2
        return False

    def AddEdge(self, v1, v2):
        # добавление ребра между вершинами v1 и v2
        pass

    def RemoveEdge(self, v1, v2):
        # удаление ребра между вершинами v1 и v2
        pass