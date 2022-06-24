from __future__ import annotations

def stalin_sort(array: list[float]) -> list[float]:
    result = [array[0]]
    for element in array[1:]:
        if element >= result[-1]:
            result.append(element)
    return result
