import copy

def gnome_sort(array: list[float]) -> list[float]:
    _array = copy.copy(array)
    position = 0
    while position < len(_array):
        if position == 0 or _array[position] >= _array[position - 1]:
            position += 1
        else:
            _array[position - 1], _array[position] = _array[position], _array[position - 1]
            position -= 1
    return _array
