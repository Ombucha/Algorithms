import collections
import copy
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

def reverse_delete_algorithm(graph: WeightedGraph) -> networkx.Graph:
    tree = networkx.Graph(copy.deepcopy(graph))
    edges = {edge: graph.get_edge_data(*edge)["weight"] for edge in graph.edges}
    edges = sorted(edges, key = edges.get, reverse = True)
    index = 0
    while index < len(edges):
        edge = edges[index]
        weight = graph.get_edge_data(*edge)["weight"]
        tree.remove_edge(*edge)
        if not networkx.is_connected(tree):
            tree.add_edge(*edge)
        index += 1
    return tree
