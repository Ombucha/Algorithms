import networkx

def depth_first_search(graph: networkx.Graph, root: str | float) -> networkx.Graph:
    tree = networkx.Graph()
    explored = []
    stack = [root]
    while len(stack) > 0:
        vertex = stack.pop(-1)
        explored.append(vertex)
        neighbours = list(graph.neighbors(vertex))
        vertices = [node for node in neighbours if node not in explored + stack]
        stack += vertices
        edges = [(vertex, child) for child in vertices]
        tree.add_edges_from(edges)
    return tree
