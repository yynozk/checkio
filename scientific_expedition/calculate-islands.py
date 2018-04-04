def rec(r, c, map):
    map[r][c] = 0
    size = 1

    for vr, vc in zip([0, 1, 1, 1, 0, -1, -1, -1], [-1, -1, 0, 1, 1, 1, 0, -1]):
        if 0 <= r+vr < len(map) and 0 <= c+vc < len(map[0]) and map[r+vr][c+vc] > 0:
            size += rec(r+vr, c+vc, map)

    return size

def checkio(land_map):
    return sorted([rec(r, c, land_map) for r, row in enumerate(land_map) for c, land in enumerate(row) if land > 0])
