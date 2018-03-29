OPERATION_NAMES = ("conjunction", "disjunction", "implication", "exclusive", "equivalence")

def n(x):
    return abs(1 - x)

def boolean(x, y, operation):
    if operation == OPERATION_NAMES[0]:
        return x & y
    elif operation == OPERATION_NAMES[1]:
        return x | y
    elif operation == OPERATION_NAMES[2]:
        return n(x) | y
    elif operation == OPERATION_NAMES[3]:
        return x ^ y
    elif operation == OPERATION_NAMES[4]:
        return n(x ^ y)
