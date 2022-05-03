import copy

def pigeonhole_sort(array: list[float]) -> list[float]:
    _array = copy.deepcopy(array)
    base = min(key for key in _array)
    size = max(key for key in _array) - base + 1
    pigeonholes = [[] for _ in range(size)]
    for key in _array:
        index = key - base
        pigeonhole = pigeonholes[index]
        pigeonhole.append(key)
    _array.clear()
    for pigeonhole in pigeonholes:
        _array.extend(pigeonhole)
    return _array
