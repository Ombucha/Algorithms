from __future__ import annotations

def fibonacci_sequence_iterative(number: int) -> list[int]:
    if number == 0:
        return [0]
    sequence = [0, 1]
    index = 2
    while index <= number:
        term = sequence[index - 1] + sequence[index - 2]
        sequence.append(term)
        index += 1
    return sequence

def fibonacci_sequence_recursive(number: int) -> list[int]:
    if number == 0:
        return [0]
    if number == 1:
        return [0, 1]
    sequence = fibonacci_sequence_recursive(number - 1)
    sequence += [sequence[-1] + sequence[-2]]
    return sequence
