import copy

def stooge_sort(array: list[float], left: int = 0, right: int = None) -> list[float]:
    _array = copy.deepcopy(array)
    if right is None:
        right = len(_array) - 1
    if _array[left] > _array[right]:
        _array[right], _array[left] = _array[left], _array[right]
    if (right - left + 1) > 2:
        index = (right - left + 1) // 3
        _array = stooge_sort(_array, left, right - index)
        _array = stooge_sort(_array, left + index, right)
        _array = stooge_sort(_array, left, right - index)
    return _array
