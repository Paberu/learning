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
                self.vertex[i] = Vertex(v)
                break

    def RemoveVertex(self, v):
        vertex_index = self.get_vertex_by_value(v)
        if vertex_index:
            for i in range(self.max_vertex):
                self.m_adjacency[vertex_index][i] = 0
                self.m_adjacency[i][vertex_index] = 0
            self.vertex[vertex_index] = None

    def IsEdge(self, v1, v2):
        v1_index = self.get_vertex_by_value(v1)
        v2_index = self.get_vertex_by_value(v2)
        if v1_index is not None and v2_index is not None:
            if self.m_adjacency[v1_index][v2_index] == 1 or self.m_adjacency[v2_index][v1_index] == 1:
                return True
        return False

    def AddEdge(self, v1, v2):
        v1_index = self.get_vertex_by_value(v1)
        v2_index = self.get_vertex_by_value(v2)
        if v1_index is not None and v2_index is not None:
            self.m_adjacency[v1_index][v2_index] = 1
            self.m_adjacency[v2_index][v1_index] = 1

    def RemoveEdge(self, v1, v2):
        v1_index = self.get_vertex_by_value(v1)
        v2_index = self.get_vertex_by_value(v2)
        if v1_index is not None and v2_index is not None:
            self.m_adjacency[v1_index][v2_index] = 0
            self.m_adjacency[v2_index][v1_index] = 0

    def get_vertex_by_value(self, v):
        for i in range(self.max_vertex):
            if self.vertex[i].Value == v:
                return i
        return None
