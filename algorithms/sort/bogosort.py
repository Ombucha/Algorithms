import copy
import random

def is_sorted(array: list[float]) -> bool:
    boolean = all(index <= _index for index, _index in zip(array, array[1:]))
    return boolean

def bogosort(array: list[float]) -> list[float]:
    _array = copy.copy(array)
    while not is_sorted(_array):
        random.shuffle(_array)
    return _array
