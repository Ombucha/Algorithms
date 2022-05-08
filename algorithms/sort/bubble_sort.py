from __future__ import annotations

import copy

def bubble_sort_iterative(array: list[float]) -> list[float]:
    _array = copy.deepcopy(array)
    length = len(_array)
    swapped = True
    while swapped:
        swapped = False
        for index in range(length - 1):
            if _array[index] > _array[index + 1]:
                _array[index], _array[index + 1] = _array[index + 1], _array[index]
                swapped = True
    return _array

def bubble_sort_recursive(array: list[float], length: int = None) -> list[float]:
    _array = copy.deepcopy(array)
    if length is None:
        length = len(_array)
    if length == 1:
        return _array
    for index in range(length - 1):
        if _array[index] > _array[index + 1]:
            _array[index], _array[index + 1] = _array[index + 1], _array[index]
    return bubble_sort_recursive(_array, length - 1)
