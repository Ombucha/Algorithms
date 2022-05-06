import typing
import networkx

def depth_first_search(graph: networkx.DiGraph, root: typing.Any, explored: list, stack: list) -> None:
    if root not in explored:
        explored.append(root)
        for vertex in graph.neighbors(root):
            depth_first_search(graph, vertex, explored, stack)
        stack.append(root)

def kosaraju_algorithm(graph: networkx.DiGraph) -> list[set]:
    stack, explored = [], []
    for vertex in graph.nodes:
        depth_first_search(graph, vertex, explored, stack)
    explored = []
    components = []
    for vertex in reversed(stack):
        if vertex not in explored:
            component = []
            depth_first_search(graph.reverse(copy = True), vertex, explored, component)
            components.append(set(component))
    return components
