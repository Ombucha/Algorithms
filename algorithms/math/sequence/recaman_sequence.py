from __future__ import annotations

def recaman_sequence_iterative(number: int) -> int:
    if number == 0:
        return [0]
    sequence = []
    for term in range(number + 1):
        if term == 0:
            sequence.append(0)
        elif (sequence[term - 1] - term > 0) and (sequence[term - 1] - term not in sequence):
            sequence.append(sequence[term - 1] - term)
        else:
            sequence.append(sequence[term - 1] + term)
    return sequence

def recaman_sequence_recursive(number: int) -> int:
    if number == 0:
        return [0]
    sequence = recaman_sequence_recursive(number - 1)
    if (sequence[number - 1] - number > 0) and (sequence[number - 1] - number not in sequence):
        sequence.append(sequence[number - 1] - number)
    else:
        sequence.append(sequence[number - 1] + number)
    return sequence
