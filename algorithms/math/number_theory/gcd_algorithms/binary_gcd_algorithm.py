def binary_gcd_algorithm(number_1: int, number_2: int) -> int:
    if number_1 == 0:
        return number_2
    if number_2 == 0:
        return number_1
    index = 0
    while (number_1 | number_2) & 1 == 0:
        number_1 >>= 1
        number_2 >>= 1
        index += 1
    while (number_1 & 1) == 0:
        number_1 >>= 1
    while number_2 != 0:
        while number_2 & 1 == 0:
            number_2 >>= 1
        if number_1 > number_2:
            number_1, number_2 = number_2, number_1
        number_2 -= number_1
    return number_1 << index
