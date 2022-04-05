def collatz_sequence_iterative(number: int) -> int:
    sequence = [number]
    term = number
    while term != 1:
        if term % 2 == 0:
            term //= 2
        else:
            term = 3 * term + 1
        sequence.append(term)
    return sequence

def collatz_sequence_recursive(number: int) -> int:
    if number == 1:
        return [1]
    sequence = [number]
    term = number
    if term % 2 == 0:
        term //= 2
    else:
        term = 3 * term + 1
    sequence += collatz_sequence_recursive(term)
    return sequence
