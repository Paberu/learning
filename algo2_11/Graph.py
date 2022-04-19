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

    def DepthFirstSearch(self, index_from, index_to):
        inner_stack = [self.vertex[index_from]]
        for vertex in self.vertex:
            vertex.hit = False
        current_v = self.vertex[index_from]
        current_index = index_from
        while len(inner_stack) != 0:
            current_v.hit = True
            had_unhit_edges = False
            for i in range(self.max_vertex):
                if self.m_adjacency[current_index][i] == 1:
                    if i == index_to:
                        inner_stack.insert(0, self.vertex[index_to])
                        return list(reversed(inner_stack))
                    else:
                        if not self.vertex[i].hit:
                            current_v = self.vertex[i]
                            inner_stack.insert(0, current_v)
                            current_index = i
                            had_unhit_edges = True
                            break
            if not had_unhit_edges:
                inner_stack.remove(current_v)
                if len(inner_stack) > 0:
                    current_v = inner_stack[0]
                    current_index = self.vertex.index(current_v)
        return list(reversed(inner_stack))

    def BreadthFirstSearch(self, index_from, index_to):
        inner_queue = [self.vertex[index_from]]
        deleted_from_queue = []
        for vertex in self.vertex:
            vertex.hit = False
        current_v = self.vertex[index_from]
        current_index = index_from
        current_v.hit = True
        while len(inner_queue) != 0:
            for i in range(self.max_vertex):
                if self.m_adjacency[current_index][i] == 1:
                    if i == index_to:
                        return self.get_list_for_return(current_index, index_to, deleted_from_queue)
                    else:
                        if not self.vertex[i].hit:
                            inner_queue.append(self.vertex[i])
                            self.vertex[i].hit = True
            deleted_from_queue.append(inner_queue.pop(0))
            if len(inner_queue) > 0:
                current_v = inner_queue[0]
                current_index = self.vertex.index(current_v)

    def get_list_for_return(self, current_index, index_to, deleted_from_queue):
        list_for_return = [self.vertex[current_index], self.vertex[index_to]]
        while current_index != 0:
            for deleted_index in deleted_from_queue:
                if self.m_adjacency[deleted_index][current_index] == 1:
                    list_for_return.insert(0, self.vertex[deleted_index])
                    current_index = deleted_index
        return list_for_return
