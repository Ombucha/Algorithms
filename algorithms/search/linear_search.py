from __future__ import annotations

import typing

def linear_search_iterative(array: list, target: typing.Any) -> int | None:
    for index, element in enumerate(array):
        if element == target:
            return index
    return None

def linear_search_recursive(array: list, target: typing.Any) -> int | None:
    length = len(array)
    if length == 1:
        if array[0] == target:
            return 0
        return None
    if array[length - 1] == target:
        return length - 1
    return linear_search_recursive(array[:length - 1], target)
