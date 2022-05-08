from __future__ import annotations

import copy
import networkx

def kahn_algorithm(graph: networkx.DiGraph) -> list:
    _graph = copy.deepcopy(graph)
    sequence = []
    vertices = [vertex for vertex in _graph.nodes if _graph.in_degree(vertex) == 0]
    while len(vertices) > 0:
        vertex = vertices[0]
        vertices.remove(vertex)
        sequence.append(vertex)
        neighbours = list(_graph.neighbors(vertex))
        for node in neighbours:
            _graph.remove_edge(vertex, node)
            if _graph.in_degree(node) == 0:
                vertices.append(node)
    return sequence
