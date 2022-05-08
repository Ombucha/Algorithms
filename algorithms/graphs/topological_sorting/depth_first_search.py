from __future__ import annotations

import random
import typing
import networkx

def depth_first_search(graph: networkx.DiGraph) -> list:

    def visit(graph: networkx.DiGraph, vertex: typing.Any, markings: dict[typing.Any, bool], sequence: list) -> None:
        if vertex in markings and markings[vertex]:
            return
        markings[vertex] = False
        for node in graph.neighbors(vertex):
            visit(graph, node, markings, sequence)
        markings[vertex] = True
        sequence.insert(0, vertex)

    sequence = []
    markings = {}
    while len(markings) < graph.number_of_nodes() or False in markings.values():
        vertex = random.choice([node for node in graph.nodes if node not in markings])
        visit(graph, vertex, markings, sequence)
    return sequence
