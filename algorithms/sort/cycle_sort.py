import copy

def cycle_sort(array: list[float]) -> list[float]:
    _array = copy.deepcopy(array)
    for index in range(0, len(_array) - 1):
        item = _array[index]
        position = index
        for _index in range(index + 1, len(_array) - 1):
            if _array[_index] < item:
                position += 1
        if position == index:
            continue
        while item == _array[position]:
            position += 1
        _array[position], item = item, _array[position]
        while position != index:
            position = index
            for _index in range(index + 1, len(_array) - 1):
                if _array[_index] < item:
                    position += 1
            while item == _array[position]:
                position += 1
            _array[position], item = item, _array[position]
    return _array
