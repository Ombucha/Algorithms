import copy

def cocktail_shaker_sort(array: list[float]) -> list[float]:
    _array = copy.deepcopy(array)
    swapped = True
    while swapped:
        swapped = False
        for index in range(len(_array) - 1):
            if _array[index] > _array[index + 1]:
                _array[index], _array[index + 1] = _array[index + 1], _array[index]
                swapped = True
        if not swapped:
            break
        swapped = False
        for index in range(len(_array) - 1):
            if _array[index] > _array[index + 1]:
                _array[index], _array[index + 1] = _array[index + 1], _array[index]
                swapped = True
    return _array
