from __future__ import annotations

import random
import sympy

def lucas_primality_test(number: int, accuracy: int = None) -> bool:
    if accuracy is None:
        accuracy = number
    factors = sympy.primefactors(number - 1)
    for _ in range(accuracy):
        integer = random.randint(2, number - 1)
        if (integer ** (number - 1)) % number != 1:
            return False
        for index, factor in enumerate(factors):
            if (integer ** ((number - 1) // factor)) % number != 1:
                if index == len(factors) - 2:
                    return True
    return False
