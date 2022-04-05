import copy

def odd_even_sort(array: list[float]):
    _array = copy.copy(array)
    sorted = False
    while not sorted:
        sorted = True
        for index in range(1, len(_array) - 1, 2):
            if _array[index] > _array[index + 1]:
                _array[index], _array[index + 1] = _array[index + 1], _array[index]
                sorted = False
        for index in range(0, len(_array) - 1, 2):
            if _array[index] > _array[index + 1]:
                _array[index], _array[index + 1] = _array[index + 1], _array[index]
                sorted = False
    return _array
