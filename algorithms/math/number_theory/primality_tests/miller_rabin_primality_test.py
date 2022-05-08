from __future__ import annotations

import random

def miller_rabin_primality_test(number: int, accuracy: int = None) -> bool:
    if accuracy is None:
        accuracy = number
    power = 0
    coefficient = number - 1
    while coefficient % 2 == 0:
        coefficient //= 2
        power += 1
    for _ in range(accuracy):
        composite = True
        integer = random.randint(2, number - 2)
        _integer = (integer ** coefficient) % number
        if _integer in (1, number - 1):
            composite = False
        for _ in range(power):
            _integer = (_integer ** 2) % number
            if _integer == number - 1:
                composite = False
        if composite:
            return False
    return True
