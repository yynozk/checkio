from functools import reduce

def checkio(str_number, radix):
    try:
        return reduce(lambda x, y: x * radix + y, map(lambda i: int(i, base=radix), str_number))
    except ValueError:
        return -1
