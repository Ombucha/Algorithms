from __future__ import annotations

import copy
import math

def american_flag_sort(array: list[int], radix: int = None) -> list[int]:

    def get_radix_value(number: int, digit: int, radix: int) -> int:
        return int(math.floor(number / radix ** digit)) % radix

    def compute_offsets(array: list[int], start: int, end: int, digit: int, radix: int) -> list[int]:
        counts = [0 for _ in range(radix)]
        for index in range(start, end):
            value = get_radix_value(array[index], digit, radix)
            counts[value] += 1
        offsets = [0 for _ in range(radix)]
        total = 0
        for index in range(radix):
            offsets[index] = total
            total += counts[index]
        return offsets

    def swap(array: list[int], offsets, start: int, digit: int, radix: int) -> None:
        index = start
        next_free = copy.deepcopy(offsets)
        block = 0
        while block < radix - 1:
            if index >= start + offsets[block + 1]:
                block += 1
                continue
            value = get_radix_value(array[index], digit, radix)
            if value == block:
                index += 1
                continue
            swap_to = start + next_free[value]
            array[index], array[swap_to] = array[swap_to], array[index]
            next_free[value] += 1

    def helper(array: list[int], start: int, end: int, digit: int, radix: int) -> None:
        offsets = compute_offsets(array, start, end, digit, radix)
        swap(array, offsets, start, digit, radix)
        if digit == 0:
            return
        for index in range(len(offsets) - 1):
            helper(array, offsets[index], offsets[index + 1], digit - 1, radix)

    if radix is None:
        radix = len(array)
    _array = copy.deepcopy(array)
    maximum_value = max(_array)
    maximum_digit = int(math.floor(math.log(maximum_value, radix)))
    helper(_array, 0, len(_array), maximum_digit, radix)
    return _array
