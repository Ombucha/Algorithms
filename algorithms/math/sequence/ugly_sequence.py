def prime_factorise(number: int) -> list[int]:
    factors = []
    factor = 2
    while number > 1:
        if number % factor == 0:
            factors.append(factor)
            number //= factor
        else:
            factor += 1
    return factors

def ugly_sequence_iterative(number: int) -> list[int]:
    sequence = []
    term = 2
    while len(sequence) != number:
        factors = set(prime_factorise(term))
        if factors.issubset({2, 3, 5}):
            sequence.append(term)
        term += 1
    return sequence

def ugly_sequence_recursive(number: int) -> list[int]:
    if number == 1:
        return [2]
    sequence = ugly_sequence_recursive(number - 1)
    term = sequence[-1] + 1
    while len(sequence) != number:
        factors = set(prime_factorise(term))
        if factors.issubset({2, 3, 5}):
            sequence.append(term)
        term += 1
    return sequence
