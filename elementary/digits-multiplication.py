from functools import reduce
import operator

def checkio(number):
    return reduce(operator.mul, map(int, list(str(number).replace("0", ""))))
