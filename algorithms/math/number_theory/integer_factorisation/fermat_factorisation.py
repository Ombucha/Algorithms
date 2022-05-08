from __future__ import annotations

import sympy

def fermat_factorisation(number: int) -> int:
    _number = sympy.ceiling(sympy.sqrt(number))
    __number = _number ** 2 - number
    while sympy.sqrt(__number) % 1 != 0:
        _number += 1
        __number = _number ** 2 - number
    factors = (int(_number - sympy.sqrt(__number)), int(_number + sympy.sqrt(__number)))
    return factors
