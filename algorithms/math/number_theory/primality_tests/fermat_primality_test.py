from __future__ import annotations

import random

def fermat_primality_test(number: int, accuracy: int = None) -> bool:
    if accuracy is None:
        accuracy = number
    for _ in range(accuracy):
        integer = random.randint(2, number - 2)
        if integer ** (number - 1) % number != 1:
            return False
    return True
