def euclidean_algorithm_iterative(number_1: int, number_2: int) -> int:
    while number_1 != number_2:
        if number_1 > number_2:
            number_1 = number_1 - number_2
        else:
            number_2 = number_2 - number_1
    return number_1

def euclidean_algorithm_recursive(number_1: int, number_2: int) -> int:
    if number_2 == 0:
        return number_1
    return euclidean_algorithm_recursive(number_2, number_1 % number_2)
