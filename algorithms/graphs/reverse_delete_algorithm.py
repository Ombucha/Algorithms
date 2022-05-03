import copy
import networkx

def reverse_delete_algorithm(graph: networkx.Graph) -> networkx.Graph:
    tree = copy.copy(graph)
    edges = {edge: graph.get_edge_data(edge[0], edge[1])["weight"] for edge in graph.edges}
    edges = sorted(edges, key = edges.get)
    index = 0
    while index < len(edges):
        edge = edges[index]
        tree.remove_edge(edge[0], edge[1])
        if not networkx.is_connected(tree):
            graph.add_edge(edge[0], edge[1])
        index += 1
    return tree
