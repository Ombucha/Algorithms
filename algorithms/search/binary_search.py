from __future__ import annotations

import math

def binary_search_recursive(array: list[float], target: float, low: int = 0, high: int = None) -> int | None:
    if high is None:
        high = len(array) - 1
    if low > high:
        return None
    middle = math.floor((low + high) / 2)
    if array[middle] == target:
        return middle
    if array[middle] < target:
        return binary_search_recursive(array, target, middle + 1, high)
    return binary_search_recursive(array, target, low, middle - 1)

def binary_search_iterative(array: list[float], target: float) -> int | None:
    low = 0
    high = len(array) - 1
    if low > high:
        return None
    while low <= high:
        middle = math.floor((low + high) / 2)
        if array[middle] < target:
            low = middle + 1
        elif array[middle] > target:
            high = middle - 1
        else:
            return middle
    return None
