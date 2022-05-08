from __future__ import annotations

import typing
import networkx

def depth_first_search(graph: networkx.Graph, root: typing.Any) -> networkx.Graph:
    tree = networkx.Graph()
    explored = []
    stack = [root]
    while len(stack) > 0:
        vertex = stack.pop()
        explored.append(vertex)
        neighbours = list(graph.neighbors(vertex))
        vertices = [node for node in neighbours if node not in explored + stack]
        stack += vertices
        edges = [(vertex, child) for child in vertices]
        tree.add_edges_from(edges)
    return tree
