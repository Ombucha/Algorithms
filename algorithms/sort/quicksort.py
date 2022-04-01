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

def quicksort_iterative(array: list[float], low: int, high: int) -> list[float]:
    _array = copy.copy(array)
    size = high - low + 1
    stack = [0] * (size)
    top = -1
    top += 1
    stack[top] = low
    top += 1
    stack[top] = high
    while top >= 0:
        high = stack[top]
        top = top - 1
        low = stack[top]
        top = top - 1
        pivot = partition(_array, low, high)
        if pivot - 1 > low:
            top = top + 1
            stack[top] = low
            top = top + 1
            stack[top] = pivot - 1
        if pivot + 1 < high:
            top = top + 1
            stack[top] = pivot + 1
            top = top + 1
            stack[top] = high
    return _array

def quicksort_recursive(array: list[float], low: int = 0, high: int = None) -> list[float]:
    _array = copy.copy(array)
    if high is None:
        high = len(array) - 1
    if low < high:
        pivot = partition(_array, low, high)
        _array = quicksort_recursive(quicksort_recursive(_array, low, pivot - 1), pivot + 1, high)
    return _array
