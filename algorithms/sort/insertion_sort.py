import copy

def insertion_sort_iterative(array: list[float]) -> list[float]:
    _array = copy.deepcopy(array)
    for index, key in enumerate(_array):
        _index = index - 1
        while _index > -1 and _array[_index] > key:
            _array[_index + 1] = _array[_index]
            _index -= 1
        _array[_index + 1] = key
    return _array

def insertion_sort_recursive(array: list[float], length: int = None) -> list[float]:
    _array = copy.deepcopy(array)
    if length is None:
        length = len(_array)
    if length == 1:
        return _array
    last_element = _array[length - 1]
    index = length - 2
    _array = insertion_sort_recursive(_array, length - 1)
    while index >= 0 and _array[index] > last_element:
        _array[index + 1] = _array[index]
        index -= 1
    _array[index + 1] = last_element
    return _array
