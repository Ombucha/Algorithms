from __future__ import annotations

import sympy

def wilson_primality_test(number: int) -> bool:
    if number in (0, 1, 4):
        return False
    if number in (2, 3):
        return True
    test = (sympy.factorial(number - 1) + 1) % number
    if test == 0:
        return True
    return False
