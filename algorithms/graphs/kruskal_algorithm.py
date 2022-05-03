import networkx

def kruskal_algorithm(graph: networkx.Graph) -> networkx.Graph:
    tree = networkx.Graph()
    tree.add_nodes_from(graph.nodes)
    edges = {edge: graph.get_edge_data(edge[0], edge[1])["weight"] for edge in graph.edges}
    while len(edges) > 0 and tree.number_of_nodes() != graph.nodes:
        edge = min(edges, key = edges.get)
        edges.pop(edge)
        if networkx.has_path(graph, edge[0], edge[1]):
            tree.add_edge(edge[0], edge[1])
    return tree