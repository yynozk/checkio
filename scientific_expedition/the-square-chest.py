def checkio(lines_list):
    ans = 0
    lines_list = list(map(sorted, lines_list))

    for i in [1, 2, 3, 5, 6, 7, 9, 10, 11]:
        square = [[i, i+1], [i, i+4], [i+1, i+5], [i+4, i+5]]
        ans += 1 if all([l in lines_list for l in square]) else 0

    for i in [1, 2, 5, 6]:
        square = [[i, i+1], [i+1, i+2], [i, i+4], [i+4, i+8],
                  [i+2, i+6], [i+6, i+10], [i+8, i+9], [i+9, i+10]]
        ans += 1 if all([l in lines_list for l in square]) else 0

    square = [[1, 2], [2, 3], [3, 4], [1, 5], [5, 9], [9, 13],
              [4, 8], [8, 12], [12, 16], [13, 14], [14, 15], [15, 16]]
    ans += 1 if all([l in lines_list for l in square]) else 0

    return ans
