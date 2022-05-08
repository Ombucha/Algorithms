from __future__ import annotations

import copy

def shellsort(array: list[float]) -> list[float]:
    _array = copy.deepcopy(array)
    gaps = [701, 301, 132, 57, 23, 10, 4, 1]
    for gap in gaps:
        for offset in range(gap):
            index = offset
            while index < len(_array):
                __array = _array[index]
                _index = index
                while _index >= gap and _array[_index - gap] > __array:
                    _array[_index] = _array[_index - gap]
                    _index -= gap
                _array[_index] = __array
                index += gap
    return _array
