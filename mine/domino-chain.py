def rec(r, matrix):
    if all([all([i == 0 for i in row]) for row in matrix]):
        return 1

    chain_count = 0

    for c, n in enumerate(matrix[r]):
        if n == 0:
            continue
        matrix[r][c] -= 1
        matrix[c][r] -= 1
        chain_count += rec(c, matrix)
        matrix[r][c] += 1
        matrix[c][r] += 1

    return chain_count


def domino_chain(tiles: str) -> int:
    matrix = [[0 for _ in range(7)] for _ in range(7)]
    for (a, b) in [pair.split("-") for pair in tiles.split(", ")]:
        matrix[int(a)][int(b)] += 1
        matrix[int(b)][int(a)] += 1

    return sum([rec(i, matrix) for i in range(7)]) / 2
