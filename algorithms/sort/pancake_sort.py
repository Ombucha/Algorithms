import copy

def pancake_sort(array: list[float]) -> list[float]:

    def flip(array: list[float], number: int) -> None:
        left = 0
        while left < number:
            array[left], array[number] = array[number], array[left]
            number -= 1
            left += 1

    def maximum_index(array: list[float], number: int) -> int:
        index = 0
        for _index in range(number):
            if array[_index] > array[index]:
                index = _index
        return index

    _array = copy.copy(array)
    length = len(_array)
    while length > 1:
        maximum = maximum_index(_array, length)
        flip(_array, maximum)
        flip(_array, length - 1)
        length -= 1
    return _array
