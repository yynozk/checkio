from itertools import combinations as C

def check_connection(network, first, second):
    groups = [set(s.split("-")) for s in network]

    loop = True
    while loop:
        loop = False
        for l, r in C(range(len(groups)), 2):
            if groups[l].intersection(groups[r]):
                lg, rg = groups[l], groups[r]
                groups.remove(lg)
                groups.remove(rg)
                groups.append(lg.union(rg))
                loop = True
                break

    return any([{first, second}.issubset(g) for g in groups])
