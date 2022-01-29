from typing import List, Tuple, Optional


def min_weight_from_vertex(vertex: Optional[int], adj_matrix: List[List[int]]) -> (int, Tuple):
    min_weight = float("inf")
    min_edges = None, None
    if not vertex:
        for i in range(len(adj_matrix)):
            for j in range(len(adj_matrix[i])):
                if adj_matrix[i][j] < min_weight:
                    min_weight = adj_matrix[i][j]
                    min_edges = i, j

    return min_weight, min_edges


def min_spanning_tree_weight(adj_matrix: List[List[int]]) -> int:
    min_weight, vertex_cache = min_weight_from_vertex(adj_matrix=adj_matrix, vertex=None)
    vertex_cache = list(vertex_cache)
    while True:
        temp = []
        min_temp
        for vertex in vertex_cache:
            temp.append(min_weight_from_vertex(vertex=vertex, adj_matrix=adj_matrix))

    return min_weight
