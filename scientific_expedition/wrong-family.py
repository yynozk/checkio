def is_family(tree):
    if len({tuple(sorted(e)) for e in tree}) != len(tree) \
        or any([e[0] == e[1] for e in tree]) \
        or len(set([e[1] for e in tree])) != len(tree):
        return False

    dic = {n: 0 for p in tree for n in p}
    for elem in tree:
        dic[elem[0]] = 1
    for elem in tree:
        dic[elem[1]] = 0
    return True if list(dic.values()).count(1) == 1 else False
