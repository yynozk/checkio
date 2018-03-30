def create_intervals(data):
    intervals = []
    for i in sorted(list(data)):
        if not intervals or i > intervals[-1][-1] + 1:
            intervals.append([i, i])
        else:
            intervals[-1][-1] = i

    return list(map(tuple, intervals))
