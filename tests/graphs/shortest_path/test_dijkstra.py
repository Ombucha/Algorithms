import pytest
import networkx as nx
from algorithms.graphs.shortest_path.dijkstra import dijkstra


def generate_sample_graph():
    graph = nx.Graph()
    graph.add_weighted_edges_from(
        [
            (1, 2, 2),
            (1, 7, 3),
            (1, 6, 7),
            (2, 1, 2),
            (2, 7, 6),
            (2, 3, 4),
            (3, 2, 4),
            (3, 8, 2),
            (3, 4, 2),
            (4, 3, 2),
            (4, 8, 8),
            (4, 5, 1),
            (5, 4, 1),
            (5, 6, 6),
            (5, 9, 2),
            (6, 5, 6),
            (6, 9, 5),
            (6, 1, 7),
            (7, 1, 3),
            (7, 2, 6),
            (7, 8, 3),
            (7, 9, 1),
            (8, 3, 2),
            (8, 4, 8),
            (8, 7, 3),
            (8, 9, 4),
            (9, 7, 1),
            (9, 6, 5),
            (9, 5, 2),
            (9, 8, 4),
        ]
    )
    return graph


def test_path_exists():
    graph = generate_sample_graph()
    assert dijkstra(graph, 6, 3) == [6, 5, 4, 3]


def test_src_not_in_graph():
    graph = generate_sample_graph()
    with pytest.raises(Exception, match="Source Is Not In Graph"):
        dijkstra(graph, 10, 3)


def test_target_not_in_graph():
    graph = generate_sample_graph()
    with pytest.raises(Exception, match="Target Is Not In Graph"):
        dijkstra(graph, 6, 10)


def test_negative_weights():
    graph = generate_sample_graph()
    graph.remove_edge(1, 2)
    graph.add_weighted_edges_from([(1, 2, -10)])

    with pytest.raises(Exception, match="Dijkstra Cannot Handle Negative Weights"):
        dijkstra(graph, 6, 3)


def test_weights_does_not_exists():
    graph = generate_sample_graph()
    graph.remove_edge(1, 2)
    graph.add_edge(1, 2)

    with pytest.raises(Exception, match="Edge Weight Cannot Be None"):
        dijkstra(graph, 6, 3)


def test_no_path():
    graph = generate_sample_graph()
    graph.remove_edge(6, 1)
    graph.remove_edge(6, 9)
    graph.remove_edge(6, 5)

    with pytest.raises(Exception, match="No Path from Source to Target"):
        dijkstra(graph, 6, 3)
