import copy
import typing

def bitonic_sort_recursive(array: list[float], low: int = 0, length: int = None, direction: typing.Literal[0, 1] = 1) -> list[float]:

    def merge(array: list[float], low: int, length: int, direction: typing.Literal[0, 1]) -> list[float]:
        _array = copy.copy(array)
        if length > 1:
            _length = length // 2
            for index in range(low , low + _length):
                if (direction == 1 and _array[index] > _array[index + _length]) or (direction == 0 and _array[index] < _array[index + _length]):
                    _array[index], _array[index + _length] = _array[index + _length], _array[index]
            _array = merge(_array, low, _length, direction)
            _array = merge(_array, low + _length, _length, direction)
        return _array

    if length is None:
        length = len(array)
    _array = copy.copy(array)
    if length > 1:
        _length = length // 2
        _array = bitonic_sort_recursive(_array, low, _length, 1)
        _array = bitonic_sort_recursive(_array, low + _length, _length, 0)
        _array = merge(_array, low, length, direction)
    return _array
