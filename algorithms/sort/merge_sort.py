import math

def merge(array_1: list[float], array_2: list[float]) -> list[float]:
    if len(array_1) == 0:
        return array_2
    if len(array_2) == 0:
        return array_1
    if array_1[0] < array_2[0]:
        return [array_1[0]] + merge(array_1[1:], array_2)
    return [array_2[0]] + merge(array_1, array_2[1:])

def merge_sort_recursive(array: list[float]) -> list[float]:
    length = len(array)
    if length == 1:
        return array
    array = merge(merge_sort_recursive(array[:math.floor(length / 2)]), merge_sort_recursive(array[math.floor(length / 2):]))
    return array
