import typing
import networkx

def prim_algorithm(graph: networkx.Graph, root: typing.Any) -> networkx.Graph:
    tree = networkx.Graph()
    vertices = set(graph.nodes)
    explored = {root}
    while explored != vertices:
        edges = {}
        for edge in set(graph.edges):
            if (edge[0] in explored and edge[1] in vertices.difference(explored)) or (edge[1] in explored and edge[0] in vertices.difference(explored)):
                edges[edge] = graph.get_edge_data(edge[0], edge[1])["weight"]
        edge = min(edges, key = edges.get)
        tree.add_edge(edge[0], edge[1])
        explored = explored.union(set(edge))
    return tree
