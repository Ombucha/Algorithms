import copy
import math

import insertion_sort
import heapsort
import quicksort

def introsort(array: list[float], maximum_depth: int = None) -> list[float]:
    if maximum_depth is None:
        maximum_depth = math.floor(math.log(len(array), 2)) * 2
    _array = copy.copy(array)
    length = len(_array)
    if length < 16:
        _array = insertion_sort.insertion_sort_iterative(_array)
    elif maximum_depth == 0:
        _array = heapsort.heapsort(_array)
    else:
        pivot = quicksort.partition(_array)
        introsort(_array[1:pivot - 1], maximum_depth - 1)
        introsort(_array[pivot + 1:length], maximum_depth - 1)
    return _array
