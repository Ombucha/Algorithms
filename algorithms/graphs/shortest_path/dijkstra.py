import math
import heapq
import typing
from collections import defaultdict
import networkx as nx


def dijkstra(graph: nx.Graph, src: typing.Any, target: typing.Any) -> list:
    print(graph.nodes)
    assert src in graph.nodes, "Source Is Not In Graph"
    assert target in graph.nodes, f"Target Is Not In Graph"

    for (u, v, weight) in graph.edges.data("weight"):
        assert weight is not None, "Edge Weight Cannot Be None"
        assert 0 <= int(weight), "Dijkstra Cannot Handle Negative Weights"

    seen = defaultdict(bool)
    dist = defaultdict(lambda: math.inf)
    parent = defaultdict(lambda: -1)

    dist[src] = 0
    pqueue = [(dist[src], src)]

    while len(pqueue) > 0:
        curr_dist, curr_node = heapq.heappop(pqueue)

        if seen[curr_node]:
            continue
        seen[curr_node] = True

        if curr_node == target:
            break

        for neighbor, _info in graph.adj[curr_node].items():
            weight = _info["weight"]
            if dist[neighbor] > curr_dist + weight:
                dist[neighbor] = dist[curr_node] + weight
                parent[neighbor] = curr_node
                heapq.heappush(pqueue, (dist[neighbor], neighbor))

    assert dist[target] != math.inf, "No Path from Source to Target"

    path = []
    curr_node = target
    while parent[curr_node] != -1:
        path.append(curr_node)
        curr_node = parent[curr_node]
    path.append(src)
    return path[::-1]
