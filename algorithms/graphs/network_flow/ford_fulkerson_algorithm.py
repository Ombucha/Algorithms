from __future__ import annotations

import collections
import copy
import typing
import networkx

class Network(networkx.DiGraph):

    def add_edge(self, u_of_edge: typing.Any, v_of_edge: typing.Any, capacity: float, **attr) -> None:
        return super().add_edge(u_of_edge, v_of_edge, capacity = capacity, flow = 0, **attr)

    def add_edges_from(self, ebunch_to_add: collections.abc.Container[tuple[typing.Any, typing.Any, dict]], **attr) -> None:
        ebunch_to_add = list(ebunch_to_add)
        if not all(len(element) == 3 and "capacity" in element[2].keys() for element in ebunch_to_add):
            raise ValueError("all edges need to have a capacity")
        for index, _ in enumerate(ebunch_to_add):
            ebunch_to_add[index][2]["flow"] = 0
        return super().add_edges_from(ebunch_to_add, **attr)

def ford_fulkerson_algorithm(network: Network, source: typing.Any, sink: typing.Any) -> networkx.DiGraph:

    def compute_residual_graph(network: networkx.DiGraph) -> networkx.DiGraph:
        residual_graph = networkx.DiGraph()
        residual_graph.add_nodes_from(network.nodes)
        for edge in network.edges:
            flow, capacity = network.get_edge_data(*edge)["flow"], network.get_edge_data(*edge)["capacity"]
            if flow < capacity:
                residual_graph.add_edge(*edge, capacity = capacity - flow)
            if flow > 0:
                residual_graph.add_edge(edge[1], edge[0], capacity = flow)
        return residual_graph

    def augment(network: networkx.DiGraph, path: list) -> None:
        path = [(path[index], path[index + 1]) for index in range(len(path) - 1)]
        bottleneck = min((network.get_edge_data(*edge)["capacity"] for edge in path))
        for edge in path:
            if edge in network.edges:
                network.get_edge_data(*edge)["flow"] += bottleneck
            else:
                network.get_edge_data(*edge)["flow"] -= bottleneck

    _network = networkx.DiGraph(copy.deepcopy(network))
    residual_graph = networkx.DiGraph(copy.deepcopy(_network))
    while networkx.has_path(residual_graph, source, sink):
        path = networkx.shortest_path(residual_graph, source, sink)
        augment(_network, path)
        residual_graph = compute_residual_graph(_network)
    return _network
