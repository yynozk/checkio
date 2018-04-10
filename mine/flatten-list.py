def flat_list(array):
    if isinstance(array, int):
        return [array]

    res = []
    for e in array:
        res.extend(flat_list(e))
    return res
