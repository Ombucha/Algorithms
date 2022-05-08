from __future__ import annotations

import collections
import math
import typing
import networkx

class WeightedGraph(networkx.Graph):

    def add_edge(self, u_of_edge: typing.Any, v_of_edge: typing.Any, weight: float, **attr) -> None:
        return super().add_edge(u_of_edge, v_of_edge, weight = weight, **attr)

    def add_edges_from(self, ebunch_to_add: collections.abc.Container[tuple[typing.Any, typing.Any, dict]], **attr) -> None:
        ebunch_to_add = list(ebunch_to_add)
        if not all(len(element) == 3 and "weight" in element[2].keys() for element in ebunch_to_add):
            raise ValueError("all edges need to have a weight")
        return super().add_edges_from(ebunch_to_add, **attr)

def dijkstra_algorithm(graph: WeightedGraph, root: typing.Any) -> networkx.Graph:
    tree = networkx.Graph()
    vertices = set(graph.nodes)
    distances = {vertex: math.inf for vertex in vertices}
    distances[root] = 0
    queue = set(graph.nodes)
    while len(queue) > 0:
        vertex = min({node: distances[node] for node in queue}, key = distances.get)
        queue.remove(vertex)
        for neighbour in graph.neighbors(vertex):
            weight = graph.get_edge_data(vertex, neighbour)["weight"]
            new_distance = distances[vertex] + weight
            if new_distance < distances[neighbour]:
                distances[neighbour] = new_distance
                tree.add_edge(vertex, neighbour, weight = weight)
    return tree
