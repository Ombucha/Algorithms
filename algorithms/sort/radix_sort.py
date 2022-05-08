from __future__ import annotations

import copy

def counting_sort(array: list[float], exponent: int) -> list[float]:
    length = len(array)
    output = [0] * (length)
    count = [0] * (10)
    for index in range(0, length):
        _index = int(array[index] // exponent)
        count[_index % 10] += 1
    for index in range(1, 10):
        count[index] += count[index - 1]
    index = length - 1
    while index >= 0:
        _index = int(array[index] // exponent)
        output[count[_index % 10] - 1] = array[index]
        count[_index % 10] -= 1
        index -= 1
    return output

def radix_sort(array: list[float]) -> list[float]:
    _array = copy.deepcopy(array)
    maximum = max(_array)
    exponent = 1
    while maximum / exponent > 1:
        _array = counting_sort(array, exponent)
        exponent *= 10
    return _array
