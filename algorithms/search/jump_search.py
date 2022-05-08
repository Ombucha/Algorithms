from __future__ import annotations

import sympy

def jump_search(array: list[float], target: float) -> int:
    length = len(array)
    index = 0
    _index = sympy.floor(sympy.sqrt(length))
    while array[min(_index, length) - 1] < target:
        index = _index
        _index += sympy.floor(sympy.sqrt(length))
        if index >= length:
            return None
    while array[index] < target:
        index += 1
        if index == min(_index, length):
            return None
    if array[index] == target:
        return index
    return None
