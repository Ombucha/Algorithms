import random

def bogobogosort(array: list[float]) -> list[float]:
    if len(array) == 1:
        return array
    _array = bogobogosort(array[:-1])
    _array.append(array[-1])
    while _array[-1] < _array[-2]:
        random.shuffle(_array)
        __array = bogobogosort(_array[:-1])
        __array.append(_array[-1])
        _array = __array
    return _array
