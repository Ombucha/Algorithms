def factorial_iterative(number: int) -> int:
    factorial = 1
    for multiplier in range(1, number + 1):
        factorial *= multiplier
    return factorial

def factorial_recursive(number: int) -> int:
    if number == 0:
        factorial = 1
    else:
        factorial = number * factorial_recursive(number - 1)
    return factorial
