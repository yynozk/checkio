def checkio(first, second):
    return ",".join(sorted(list(set(first.split(",")).intersection(set(second.split(","))))))
