import math

def next_sort(array: list[float]) -> list[float]:
    for index, key in enumerate(array):
        _index = index - 1
        while _index > -1 and array[_index] > key:
            array[_index + 1] = array[_index]
            _index -= 1
        array[_index + 1] = key
    return array

def bucket_sort(array: list[float], number: int = None) -> list[float]:
    if number is None:
        number = len(array)
    buckets = [[] for _ in range(number)]
    maximum = max(array)
    for index in range(len(array)):
        buckets[math.floor((number * array[index]) / maximum) - 1].append(array[index])
    for index in range(number):
        next_sort(buckets[index])
    output = []
    for index in range(number):
        output += buckets[index]
    return output
