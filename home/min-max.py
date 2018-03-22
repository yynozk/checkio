def compare(new, now, key, max_or_min):
    if key != None:
        new = key(new)
        now = key(now)

    if max_or_min == "max":
        return new > now
    elif max_or_min == "min":
        return new < now


def checkio(max_or_min, *args, **kwargs):
    key = kwargs.get("key", None)

    it = args[0] if len(args) == 1 else [i for i in args]
    val = None
    for i in it:
        if val is None or compare(i, val, key, max_or_min):
            val = i

    return val


def min(*args, **kwargs):
    return checkio("min", *args, **kwargs)


def max(*args, **kwargs):
    return checkio("max", *args, **kwargs)
