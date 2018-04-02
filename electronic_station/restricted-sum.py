def rec(data):
    if len(data) >= 2:
        data.append(data.pop() + data.pop())
        return rec(data)
    else:
        return data.pop()

def checkio(data):
    return rec(data)
