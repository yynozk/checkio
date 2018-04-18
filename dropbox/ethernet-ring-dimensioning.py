import math

ETHERNET = (100, 40, 10, 1, 0.1) # Ethernet bandwidth capacity in Gbps

def checkio(ring, *flows):
    repring = ring + ring
    flow = {frozenset((repring)[i:i + 2]): 0 for i in range(len(ring))}

    for route, amount in flows:
        begin, end = repring.index(route[0]), repring.index(route[1])
        if begin > end:
            end = repring.rindex(route[1])
        if end - begin > len(ring) / 2:
            begin, end = end, repring.rindex(route[0])
        begin, end = min(begin, end), max(begin, end)
        for i in range(begin, end):
            flow[frozenset(repring[i:i + 2])] += amount

    links = [0] * len(ETHERNET)
    for sum in flow.values():
        if sum > 100:
            links[0] += math.ceil(sum / 100)
        elif sum > 0:
            idx = [c >= sum for c in ETHERNET].count(True)
            links[idx - 1] += 1

    return links
