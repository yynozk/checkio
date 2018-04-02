def checkio(number):
    digits = []
    for i in range(9, 1, -1):
        while number % i == 0:
            number //= i
            digits.append(i)

    return int("".join(map(str, digits[::-1]))) if number == 1 else 0
