def checkio(expression):
    stack = []
    for c in expression:
        if c in ["{", "(", "["]:
            stack.append(c)
        elif c == "}" and not (stack and stack.pop() == "{"):
            return False
        elif c == ")" and not (stack and stack.pop() == "("):
            return False
        elif c == "]" and not (stack and stack.pop() == "["):
            return False

    return False if stack else True
