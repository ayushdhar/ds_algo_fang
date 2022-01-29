from typing import List, Any


class Vertex:
    def __init__(self, label: int):
        self.label = label
        self.was_visited = False


class Graph:
    @staticmethod
    def init_adj_matrix(max_vertices):
        res = []

        for i in range(max_vertices):
            row = []
            for j in range(max_vertices):
                row.append(0)
            res.append(row)
        return res

    def __init__(self, max_vertices: int):
        self.vertex_list: List[Vertex] = []
        self.adj_matrix = self.init_adj_matrix(max_vertices)
        self.max_vertices = max_vertices

    def add_vertex(self, vertex: Vertex):
        if len(self.vertex_list) < self.max_vertices:
            self.vertex_list.append(vertex)
        else:
            print("vertex list full")

    def add_edge(self, vertex1: Vertex, vertex2: Vertex):
        self.adj_matrix[vertex1.label][vertex2.label] = 1
        self.adj_matrix[vertex2.label][vertex1.label] = 1
    def dfs(self):


gp = Graph(max_vertices=4)
vertex_a, vertex_b, vertex_c, vertex_d = Vertex(0), Vertex(1), Vertex(2), Vertex(3),
gp.add_vertex(vertex_a)
gp.add_vertex(vertex_b)
gp.add_vertex(vertex_c)
gp.add_vertex(vertex_d)

gp.add_edge(vertex_a, vertex_b)
gp.add_edge(vertex_a, vertex_c)
gp.add_edge(vertex_a, vertex_d)
gp.add_edge(vertex_b, vertex_d)


print(gp.adj_matrix)
