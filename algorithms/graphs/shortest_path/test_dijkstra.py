import pytest
from dijkstra import dijkstra_adj_list


def test_path_exists():
    adj_list = [
        [(2, 2), (7, 3), (6, 7)],
        [(1, 2), (7, 6), (3, 4)],
        [(2, 4), (8, 2), (4, 2)],
        [(3, 2), (8, 8), (5, 1)],
        [(4, 1), (6, 6), (9, 2)],
        [(5, 6), (9, 5), (1, 7)],
        [(1, 3), (2, 6), (8, 3), (9, 1)],
        [(3, 2), (4, 8), (7, 3), (9, 4)],
        [(7, 1), (6, 5), (5, 2), (8, 4)],
    ]

    assert dijkstra_adj_list(9, adj_list, 6, 3) == [6, 5, 4, 3]


def test_adj_list_incomplete():
    adj_list = [
        [(2, 2), (7, 3), (6, 7)],
        [(1, 2), (7, 6), (3, 4)],
        [(2, 4), (8, 2), (4, 2)],
        [(3, 2), (8, 8), (5, 1)],
        [(4, 1), (6, 6), (9, 2)],
        [(5, 6), (9, 5), (1, 7)],
        [(1, 3), (2, 6), (8, 3), (9, 1)],
        [(3, 2), (4, 8), (7, 3), (9, 4)],
    ]

    with pytest.raises(Exception, match="incomplete"):
        dijkstra_adj_list(9, adj_list, 6, 3)


def test_adj_list_src_out_of_bounds():
    adj_list = [
        [(2, 2), (7, 3), (6, 7)],
        [(1, 2), (7, 6), (3, 4)],
        [(2, 4), (8, 2), (4, 2)],
        [(3, 2), (8, 8), (5, 1)],
        [(4, 1), (6, 6), (9, 2)],
        [(5, 6), (9, 5), (1, 7)],
        [(1, 3), (2, 6), (8, 3), (9, 1)],
        [(3, 2), (4, 8), (7, 3), (9, 4)],
        [(7, 1), (6, 5), (5, 2), (8, 4)],
    ]

    with pytest.raises(Exception, match=".* Source .* bounds"):
        dijkstra_adj_list(9, adj_list, 10, 3)


def test_adj_list_target_out_of_bounds():
    adj_list = [
        [(2, 2), (7, 3), (6, 7)],
        [(1, 2), (7, 6), (3, 4)],
        [(2, 4), (8, 2), (4, 2)],
        [(3, 2), (8, 8), (5, 1)],
        [(4, 1), (6, 6), (9, 2)],
        [(5, 6), (9, 5), (1, 7)],
        [(1, 3), (2, 6), (8, 3), (9, 1)],
        [(3, 2), (4, 8), (7, 3), (9, 4)],
        [(7, 1), (6, 5), (5, 2), (8, 4)],
    ]

    with pytest.raises(Exception, match=".* Target .* bounds"):
        dijkstra_adj_list(9, adj_list, 6, 10)


def test_adj_list_neighbors_out_of_bounds():
    adj_list = [
        [(2, 2), (7, 3), (6, 7)],
        [(1, 2), (7, 6), (3, 4)],
        [(10, 4), (8, 2), (4, 2)],
        [(3, 2), (8, 8), (5, 1)],
        [(4, 1), (6, 6), (9, 2)],
        [(5, 6), (9, 5), (1, 7)],
        [(1, 3), (2, 6), (8, 3), (9, 1)],
        [(3, 2), (4, 8), (7, 3), (9, 4)],
        [(7, 1), (6, 5), (5, 2), (8, 4)],
    ]

    with pytest.raises(Exception, match=".* Adj List .* out of bounds"):
        dijkstra_adj_list(9, adj_list, 6, 3)


def test_adj_list_negative_weights():
    adj_list = [
        [(2, 2), (7, 3), (6, 7)],
        [(1, 2), (7, 6), (3, 4)],
        [(2, 4), (8, 2), (4, 2)],
        [(3, 2), (8, 8), (5, 1)],
        [(4, 1), (6, 6), (9, 2)],
        [(5, 6), (9, 5), (1, 7)],
        [(1, 3), (2, 6), (8, 3), (9, 1)],
        [(3, 2), (4, 8), (7, 3), (9, 4)],
        [(7, 1), (6, 5), (5, 2), (8, -10)],
    ]

    with pytest.raises(Exception, match="Negative"):
        dijkstra_adj_list(9, adj_list, 6, 3)


def test_no_path():
    adj_list = [
        [(2, 2), (7, 3), (6, 7)],
        [(1, 2), (7, 6), (3, 4)],
        [(2, 4), (8, 2), (4, 2)],
        [(3, 2), (8, 8), (5, 1)],
        [(4, 1), (6, 6), (9, 2)],
        [],
        [(1, 3), (2, 6), (8, 3), (9, 1)],
        [(3, 2), (4, 8), (7, 3), (9, 4)],
        [(7, 1), (6, 5), (5, 2), (8, 4)],
    ]

    with pytest.raises(Exception, match="No Path from Source to Target"):
        dijkstra_adj_list(9, adj_list, 6, 3)
