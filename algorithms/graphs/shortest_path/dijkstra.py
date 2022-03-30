import math
import heapq


def dijkstra_adj_list(
    n: int, adj_list: list[list[tuple[int, int]]], src: int, target: int
) -> list[int]:
    assert n == len(adj_list), "The Adj List is incomplete"
    assert 1 <= src <= n, "The Source node is out of bounds"
    assert 1 <= target <= n, "The Target node is out of bounds"

    for node in range(0, n):
        for neighbor, weight in adj_list[node]:
            assert (
                1 <= neighbor <= n
            ), "The Adj List contains node(s) which is / are out of bounds"
            assert 0 <= weight, "Dijkstra Cannot Handle Negative Weights"

    # 0 based indexing
    src -= 1
    target -= 1

    seen = [False for _ in range(n)]
    parent = [-1 for _ in range(n)]
    dist = [math.inf for _ in range(n)]

    dist[src] = 0
    pqueue = [(dist[src], src)]

    while len(pqueue) > 0:
        curr_dist, curr_node = heapq.heappop(pqueue)

        if seen[curr_node]:
            continue
        seen[curr_node] = True

        if curr_node == target:
            break

        for _neighbor, weight in adj_list[curr_node]:
            neighbor = _neighbor - 1
            if dist[neighbor] > curr_dist + weight:
                dist[neighbor] = dist[curr_node] + weight
                parent[neighbor] = curr_node
                heapq.heappush(pqueue, (dist[neighbor], neighbor))

    assert dist[target] != math.inf, "No Path from Source to Target"

    path = []
    curr_node = target
    while parent[curr_node] != -1:
        path.append(curr_node + 1)
        curr_node = parent[curr_node]
    path.append(src + 1)
    return path[::-1]
