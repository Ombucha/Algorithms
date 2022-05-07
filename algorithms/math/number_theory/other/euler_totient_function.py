import math

def euler_totient_function(number: int) -> int:
    coprimes = []
    for index in range(1, number + 1):
        if math.gcd(number, index) == 1:
            coprimes.append(index)
    return len(coprimes)
