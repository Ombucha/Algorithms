import copy
import random

def bozosort(array: list[float]) -> list[float]:

    def is_sorted(array: list[float]) -> bool:
        boolean = all(index <= _index for index, _index in zip(array, array[1:]))
        return boolean

    _array = copy.deepcopy(array)
    while not is_sorted(_array):
        elements = random.sample(range(len(_array)), k = 2)
        _array[elements[0]], _array[elements[1]] = _array[elements[1]], _array[elements[0]]
    return _array
