def collatz_sequence(number: int) -> int:
    sequence = [number]
    term = number
    while term != 1:
        if term % 2 == 0:
            term //= 2
        else:
            term = 3 * term + 1
        sequence.append(term)
    return sequence
