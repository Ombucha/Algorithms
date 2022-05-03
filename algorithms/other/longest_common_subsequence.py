def maximum_length_recursive(array_1: list, array_2: list, index_1: int = None, index_2: int = None) -> list:
    if index_1 is None:
        index_1 = len(array_1)
    if index_2 is None:
        index_2 = len(array_2)
    if index_1 == 0 or index_2 == 0:
        return 0
    if array_1[index_1 - 1] == array_2[index_2 - 1]:
        return 1 + maximum_length_recursive(array_1, array_2, index_1 - 1, index_2 - 1)
    length = max(maximum_length_recursive(array_1, array_2, index_1, index_2 - 1), maximum_length_recursive(array_1, array_2, index_1 - 1, index_2))
    return length

def maximum_length_dynamic(array_1: list, array_2: list) -> int:
    length_1, length_2 = len(array_1), len(array_2)
    lengths = [[None for _ in range(length_2 + 1)] for _ in range(length_1 + 1)]
    for index in range(length_1 + 1):
        lengths[index][0] = 0
    for index in range(length_2 + 1):
        lengths[0][index] = 0
    for index in range(1, length_1 + 1):
        for _index in range(1, length_2 + 1):
            if array_1[index - 1] == array_2[_index - 1]:
                lengths[index][_index] = lengths[index - 1][_index - 1] + 1
            else:
                lengths[index][_index] = max(lengths[index - 1][_index], lengths[index][_index - 1])
    return lengths[length_1][length_2]

def longest_common_subsequence(array_1: list, array_2: list) -> list:
    sequence = []
    index, _index = len(array_1) - 1, len(array_2) - 1
    while index >= 0 and _index >= 0:
        if array_1[index] == array_2[_index]:
            sequence.insert(0, array_1[index])
            index -= 1
            _index -= 1
        elif maximum_length_recursive(array_1, array_2, index, _index) == maximum_length_recursive(array_1, array_2, index - 1, _index):
            index -= 1
        else:
            _index -= 1
    return sequence
