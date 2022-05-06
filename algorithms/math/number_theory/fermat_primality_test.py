import random

def fermat_primality_test(number: int, iterations: int = None) -> bool:
    if iterations is None:
        iterations = number
    for _ in range(iterations):
        integer = random.randint(2, number - 2)
        if integer ** (number - 1) % number != 1:
            return False
    return True