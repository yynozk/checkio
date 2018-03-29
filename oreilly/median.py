def checkio(data):
    a, l = sorted(data), len(data)
    if l % 2 == 0:
        return (a[l // 2 - 1] + a[l // 2]) / 2
    else:
        return a[l // 2]
