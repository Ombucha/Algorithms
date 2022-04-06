def fibonacci_search(array: list[float], target: float):
    length = len(array)
    __number = 0
    _number = 1
    number = __number + _number
    while number < length:
        __number = _number
        _number = number
        number = __number + _number
    offset = -1
    while number > 1:
        index = min(offset + __number, length - 1)
        if array[index] < target:
            number = _number
            _number = __number
            __number = number - _number
            offset = index
        elif array[index] > target:
            number = __number
            _number = _number - __number
            __number = number - _number
        else:
            return index
    if _number and array[length - 1] == target:
        return length - 1
    return None
