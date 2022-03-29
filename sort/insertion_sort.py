def insertion_sort_iterative(array: list[float]) -> list[float]:
    for index, key in enumerate(array):
        _index = index - 1
        while _index > -1 and array[_index] > key:
            array[_index + 1] = array[_index]
            _index -= 1
        array[_index + 1] = key
    return array
