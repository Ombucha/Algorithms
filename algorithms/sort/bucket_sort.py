import math

def bucket_sort(array: list[float], number: int = None) -> list[float]:
    if number is None:
        number = len(array)
    buckets = [[] for _ in range(number)]
    maximum = max(array)
    for index in range(len(array)):
        buckets[math.floor((number * array[index]) / maximum) - 1].append(array[index])
    for index in range(number):
        buckets[index].sort()
    output = []
    for index in range(number):
        output += buckets[index]
    return output
