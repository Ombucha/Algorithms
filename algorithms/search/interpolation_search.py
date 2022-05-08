from __future__ import annotations

def interpolation_search_iterative(array: list[int], target: int) -> int:
    low = 0
    high = len(array) - 1
    while array[high] != array[low] and target >= array[low] and target <= array[high]:
        mid = low + ((target - array[low]) * (high - low) // (array[high] - array[low]))
        if array[mid] < target:
            low = mid + 1
        elif target < array[mid]:
            high = mid - 1
        else:
            return mid
    if target == array[low]:
        return low
    return None

def interpolation_search_recursive(array: list[int], target: int, low: int = 0, high: int = None) -> int:
    if high is None:
        high = len(array) - 1
    if low <= high and target >= array[low] and target <= array[high]:
        position = low + ((high - low) // (array[high] - array[low]) * (target - array[low]))
        if array[position] == target:
            return position
        if array[position] < target:
            return interpolation_search_recursive(array, target, position + 1, high)
        if array[position] > target:
            return interpolation_search_recursive(array, target, low, position - 1)
    return None
