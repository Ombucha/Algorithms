import binary_search

def exponential_search(array: list[float], target: float) -> int:
    length = len(array)
    bound = 1
    while bound < length and array[bound] < target:
        bound *= 2
    index = binary_search.binary_search_recursive(array, target, bound / 2, min(bound + 1, length))
    return index
