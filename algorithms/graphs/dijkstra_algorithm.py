import math
import networkx

def dijkstra_algorithm(graph: networkx.Graph, root: str | float) -> networkx.Graph:
    tree = networkx.Graph()
    vertices = set(graph.nodes)
    distances = {vertex: math.inf for vertex in vertices}
    distances[root] = 0
    explored = set()
    while explored != vertices:
        vertex = min({node: distances[node] for node in vertices.difference(explored)}, key = distances.get)
        explored.add(vertex)
        for neighbour in graph.neighbors(vertex):
            weight = graph.get_edge_data(vertex, neighbour)["weight"]
            new_distance = distances[vertex] + weight
            if distances[neighbour] > new_distance:
                distances[neighbour] = new_distance
                tree.add_edge(vertex, neighbour, weight = weight)
    return tree
