import collections
import random
import typing
import networkx

class WeightedGraph(networkx.Graph):

    def add_edge(self, u_of_edge: typing.Any, v_of_edge: typing.Any, weight: float, **attr):
        return super().add_edge(u_of_edge, v_of_edge, weight = weight, **attr)

    def add_edges_from(self, ebunch_to_add: collections.abc.Container[tuple[typing.Any, typing.Any, dict]], **attr):
        ebunch_to_add = list(ebunch_to_add)
        if not all(len(element) == 3 and "weight" in element[2].keys() for element in ebunch_to_add):
            raise ValueError("all edges need to have a weight")
        return super().add_edges_from(ebunch_to_add, **attr)

def prim_algorithm(graph: WeightedGraph, root: typing.Any = None) -> networkx.Graph:
    if root is None:
        root = random.choice(list(graph.nodes))
    tree = networkx.Graph()
    vertices = set(graph.nodes)
    explored = {root}
    while explored != vertices:
        edges = {}
        for edge in set(graph.edges):
            if (edge[0] in explored and edge[1] in vertices.difference(explored)) or (edge[1] in explored and edge[0] in vertices.difference(explored)):
                edges[edge] = graph.get_edge_data(*edge)["weight"]
        edge = min(edges, key = edges.get)
        tree.add_edge(*edge)
        explored = explored.union(set(edge))
    return tree
