def count_neighbours(grid, row, col):
    r_len, c_len = len(grid), len(grid[0])
    r_range, c_range = range(row-1, row+2), range(col-1, col+2)
    neighbours = [grid[r][c] for r in r_range for c in c_range if 0 <= r < r_len and 0 <= c < c_len]
    return sum(neighbours) - grid[row][col]
