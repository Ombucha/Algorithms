from __future__ import annotations

def counting_sort(array: list[int], number: int = None) -> list[int]:
    if number is None:
        number = len(array)
    count = (number + 1) * [0]
    output = len(array) * [0]
    for value in array:
        count[value] += 1
    for index in range(number):
        count[index + 1] += count[index]
    for index in range(len(array) - 1, -1, -1):
        value = array[index]
        count[value] -= 1
        output[count[value]] = array[index]
    return output
