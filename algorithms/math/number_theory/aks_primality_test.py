def aks_primality_test(number: int) -> bool:

    def calculate_coefficients(number: int) -> list[int]:
        coefficients = [0] * (number + 1)
        coefficients[0] = 1
        for index in range(number):
            coefficients[index + 1] = 1
            for _index in range(index, 0, -1):
                coefficients[_index] = coefficients[_index - 1] - coefficients[_index]
            coefficients[0] = - coefficients[0]
        return coefficients

    coefficients = calculate_coefficients(number)
    coefficients[0] = coefficients[0] + 1
    coefficients[n] = coefficients[number] - 1
    index = number
    while index > -1 and coefficients[index] % number == 0:
        index -= 1
    return True if index < 0 else False
