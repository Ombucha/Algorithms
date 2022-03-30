import copy

def partition(array: list[float], low: int, high: int) -> int:
    pivot = array[high]
    _pivot = low - 1
    for index in range(low, high):
        if array[index] <= pivot:
            _pivot += 1
            array[_pivot], array[index] = array[index], array[_pivot]
    array[_pivot + 1], array[high] = array[high], array[_pivot + 1]
    return _pivot + 1

def quicksort_recursive(array: list[float], low: int = 0, high: int = None) -> list[float]:
    _array = copy.copy(array)
    if high is None:
        high = len(array) - 1
    if low < high:
        pivot = partition(_array, low, high)
        _array = quicksort_recursive(quicksort_recursive(_array, low, pivot - 1), pivot + 1, high)
    return _array
