from itertools import combinations as C

def break_rings(rings):
    N = max([max(e) for e in rings])

    for cnt in range(2, N):
        for breaked in C(range(1, N+1), cnt):
            if all([(r[0] in breaked) or (r[1] in breaked) for r in map(list, rings)]):
                return cnt
