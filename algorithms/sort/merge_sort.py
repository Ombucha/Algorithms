from __future__ import annotations

import copy
import math

def merge_sort_iterative(array: list[float]) -> list[float]:

    def merge(array, left, middle, right):
        _array = copy.deepcopy(array)
        value = middle - left + 1
        _value = right - middle
        _left = [0] * value
        _right = [0] * _value
        for index in range(0, value):
            _left[index] = _array[left + index]
        for index in range(0, _value):
            _right[index] = _array[middle + index + 1]
        index, _index, __index = 0, 0, left
        while index < value and _index < _value:
            if _left[index] <= _right[_index]:
                _array[__index] = _left[index]
                index += 1
            else:
                _array[__index] = _right[_index]
                _index += 1
            __index += 1
        while index < value:
            _array[__index] = _left[index]
            index += 1
            __index += 1
        while _index < _value:
            _array[__index] = _right[_index]
            _index += 1
            __index += 1
        return _array

    _array = copy.deepcopy(array)
    width = 1
    length = len(_array)
    while width < length:
        left = 0
        while left < length:
            right = min(left + (width * 2 - 1), length - 1)
            middle = min(left + width - 1, length - 1)
            _array = merge(_array, left, middle, right)
            left += width * 2
        width *= 2
    return _array

def merge_sort_recursive(array: list[float]) -> list[float]:

    def merge(array_1: list[float], array_2: list[float]) -> list[float]:
        if len(array_1) == 0:
            return array_2
        if len(array_2) == 0:
            return array_1
        if array_1[0] < array_2[0]:
            return [array_1[0]] + merge(array_1[1:], array_2)
        return [array_2[0]] + merge(array_1, array_2[1:])

    length = len(array)
    if length == 1:
        return array
    left_subarray = merge_sort_recursive(array[:math.floor(length / 2)])
    right_subarray = merge_sort_recursive(array[math.floor(length / 2):])
    _array = merge(left_subarray, right_subarray)
    return _array
