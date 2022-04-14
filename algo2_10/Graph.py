from _operator import index


class Vertex:

    def __init__(self, val):
        self.Value = val
        self.hit = False


class SimpleGraph:

    def __init__(self, size):
        self.max_vertex = size
        self.m_adjacency = [[0] * size for _ in range(size)]
        self.vertex = [None] * size

    def AddVertex(self, v):
        for i in range(self.max_vertex):
            if self.vertex[i] is None:
                self.vertex[i] = Vertex(v)
                return True
        return False

    def RemoveVertex(self, v):
        if v < self.max_vertex:
            for i in range(self.max_vertex):
                self.m_adjacency[v][i] = 0
                self.m_adjacency[i][v] = 0
            self.vertex[v] = None
            return True
        return False

    def IsEdge(self, v1, v2):
        if v1 < self.max_vertex and v2 < self.max_vertex:
            if self.m_adjacency[v1][v2] == 1 or self.m_adjacency[v2][v1] == 1:
                return True
        return False

    def AddEdge(self, v1, v2):
        if v1 < self.max_vertex and v2 < self.max_vertex:
            self.m_adjacency[v1][v2] = 1
            self.m_adjacency[v2][v1] = 1
            return True
        return False

    def RemoveEdge(self, v1, v2):
        if v1 < self.max_vertex and v2 < self.max_vertex:
            self.m_adjacency[v1][v2] = 0
            self.m_adjacency[v2][v1] = 0
            return True
        returnFalse

    def DepthFirstSearch(self, v_from, v_to):
        inner_stack = [v_from]
        for vertex in self.vertex:
            vertex.hit = False
        current_v = v_from
        current_index = self.vertex.index(v_from)
        while len(inner_stack) != 0:
            current_v.hit = True
            had_unhit_edges = False
            for i in range(self.max_vertex):
                if self.m_adjacency[current_index][i] == 1:
                    if self.vertex == v_to:
                        inner_stack.insert(0, v_to)
                        return inner_stack
                    else:
                        if not self.vertex[i].hit:
                            current_v = self.vertex[i]
                            inner_stack.insert(0, current_v)
                            current_index = self.vertex.index(current_v)
                            had_unhit_edges = True
                            break
            if not had_unhit_edges:
                inner_stack.remove(current_v)
                if len(inner_stack) > 0:
                    current_v = inner_stack[0]
        return inner_stack
