from __future__ import annotations

import copy

def slowsort(array: list[float], left: int = 0, right: int = None) -> list[float]:
    if right is None:
        right = len(array) - 1
    if left >= right:
        return array
    _array = copy.deepcopy(array)
    middle = (left + right) // 2
    _array = slowsort(_array, left, middle)
    _array = slowsort(_array, middle + 1, right)
    if _array[right] < _array[middle]:
        _array[right], _array[middle] = _array[middle], _array[right]
    _array = slowsort(_array, left, right - 1)
    return _array
