from __future__ import annotations

import sympy

def euler_totient_function(number: int) -> int:
    coprimes = []
    for index in range(1, number + 1):
        if sympy.gcd(number, index) == 1:
            coprimes.append(index)
    return len(coprimes)
