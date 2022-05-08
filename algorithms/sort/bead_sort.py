from __future__ import annotations

def bead_sort(array: list[int]) -> list[int]:
    output = []
    transposed_array = [0] * max(array)
    for number in array:
        transposed_array[:number] = [element + 1 for element in transposed_array[:number]]
    for _ in array:
        output.append(sum(n > 0 for n in transposed_array))
        transposed_array = [n - 1 for n in transposed_array]
    return output
