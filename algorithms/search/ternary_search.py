from __future__ import annotations

def ternary_search_recursive(array: list[float], target: float, low: int = 0, high: int = None) -> int:
    if high is None:
        high = len(array) - 1
    if low > high:
        return None
    one_third = low + (high - low) // 3
    two_thirds = high - (high - low) // 3
    if array[one_third] == target:
        return one_third
    if array[two_thirds] == target:
        return two_thirds
    if target < array[one_third]:
        return ternary_search_recursive(array, target, low, one_third - 1)
    if target > array[two_thirds]:
        return ternary_search_recursive(array, target, two_thirds + 1, high)
    return ternary_search_recursive(array, target, one_third + 1, two_thirds - 1)

def ternary_search_iterative(array: list[float], target: float, low: int = 0, high: int = None) -> int:
    if high is None:
        high = len(array) - 1
    while high >= low:
        one_third = low + (high - low) // 3
        two_thirds = high - (high - low) // 3
        if array[one_third] == target:
            return one_third
        if array[two_thirds] == target:
            return two_thirds
        if target < array[one_third]:
            high = one_third - 1
        elif target > array[two_thirds]:
            low = two_thirds + 1
        else:
            low = one_third + 1
            high = two_thirds - 1
    return None
