import copy

def selection_sort_iterative(array: list[float]) -> list[float]:
    _array = copy.copy(array)
    for index, _ in enumerate(_array):
        minimum = index
        for _index in range(index + 1, len(_array)):
            if _array[minimum] > _array[_index]:
                minimum = _index      
        _array[index], _array[minimum] = _array[minimum], _array[index]
    return _array

def selection_sort_recursive(array: list[float], length: int = None, index: int = 0) -> list[float]:

    def minimum_index(array: list[float], left: int, right: int) -> int:
        if left == right:
            return left
        minimum = minimum_index(array, left + 1, right)
        if array[left] < array[minimum]:
            return left
        return minimum

    _array = copy.copy(array)
    if length is None:
        length = len(_array)
    if index == length:
        return _array
    minimum = minimum_index(_array, index, length - 1)
    if minimum != index:
        array[minimum], array[index] = array[index], array[minimum]
    _array = selection_sort_recursive(array, length, index + 1)
    return _array
