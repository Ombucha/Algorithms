import collections
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

def kruskal_algorithm(graph: WeightedGraph) -> networkx.Graph:
    tree = networkx.Graph()
    tree.add_nodes_from(graph.nodes)
    edges = {edge: graph.get_edge_data(*edge)["weight"] for edge in graph.edges}
    while len(edges) > 0 and tree.number_of_nodes() != graph.nodes:
        edge = min(edges, key = edges.get)
        edges.pop(edge)
        if not networkx.has_path(tree, *edge):
            tree.add_edge(*edge, weight = graph.get_edge_data(*edge)["weight"])
    return tree
