from itertools import groupby

def checkio(matrix):
    lines, n = matrix, len(matrix)
    lines.extend([[matrix[r][c] for r in range(n)] for c in range(n) ])
    lines.extend([[matrix[j][i+j] for j in range(n - i)] for i in range(n - 3)])
    lines.extend([[matrix[i+j][j] for j in range(n - i)] for i in range(n - 3)])
    lines.extend([[matrix[j][-i-j-1] for j in range(n - i)] for i in range(n - 3)])
    lines.extend([[matrix[i+j][-j-1] for j in range(n - i)] for i in range(n - 3)])

    return True if max([len(list(g)) for l in map(groupby, lines) for k, g in l]) >= 4 else False
