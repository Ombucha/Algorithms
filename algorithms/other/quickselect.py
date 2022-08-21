from __future__ import annotations

def partition(array: list[float], low: int, high: int):
    value = array[high]
    index = low
    for _index in range(index, high):
        if array[_index] <= value:
            array[index], array[_index] = array[_index], array[index]
            index += 1
    array[index], array[high] = array[high], array[index]
    return index

def quickselect(array: list[float], index: int, low: int = 0, high: int = None) -> float:
    if high is None:
        high = len(array) - 1
    if 0 < index <= high - low + 1:
        pivot = partition(array, low, high)
        if index - 1 == pivot - low:
            return array[pivot]
        if index - 1 < pivot - low:
            return quickselect(array, index, low, pivot - 1)
        return quickselect(array, index - pivot + low - 1, pivot + 1, high)
    return None
