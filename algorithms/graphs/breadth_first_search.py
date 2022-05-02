import networkx

def breadth_first_search(graph: networkx.Graph, root: str | float) -> networkx.Graph:
    tree = networkx.DiGraph()
    explored = []
    queue = [root]
    while len(queue) > 0:
        vertex = queue.pop(0)
        explored.append(vertex)
        neighbours = list(graph.neighbors(vertex))
        vertices = [node for node in neighbours if node not in explored + queue]
        queue += vertices
        edges = [(vertex, child) for child in vertices]
        tree.add_edges_from(edges)
    return tree
