import copy

def heapsort(array: list[float]) -> list[float]:

    def heapify(array: list[float], length: int, index: int) -> None:
        largest = index
        left = 2 * index + 1
        right = 2 * index + 2
        if left < length and array[largest] < array[left]:
            largest = left
        if right < length and array[largest] < array[right]:
            largest = right
        if largest != index:
            array[index], array[largest] = array[largest], array[index]
            heapify(array, length, largest)

    _array = copy.copy(array)
    length = len(_array)
    for index in range(length // 2 - 1, -1, -1):
        heapify(_array, length, index)
    for index in range(length - 1, 0, -1):
        _array[index], _array[0] = _array[0], _array[index]
        heapify(_array, index, 0)
    return _array
