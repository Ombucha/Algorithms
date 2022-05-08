from __future__ import annotations

def karatsuba_algorithm(number_1: int, number_2: int) -> int:
    if len(str(number_1)) == 1 or len(str(number_2)) == 1:
        return number_1 * number_2
    size = min(len(str(number_1)), len(str(number_2))) // 2
    high, low = number_1 // 10 ** size, number_1 % 10 ** size
    _high, _low = number_2 // 10 ** size, number_2 % 10 ** size
    number = karatsuba_algorithm(low, _low)
    _number = karatsuba_algorithm(low + high, _low + _high)
    __number = karatsuba_algorithm(high, _high)
    answer = (__number * 10 ** (size * 2)) + ((_number - __number - number) * 10 ** size) + number
    return answer
