def checkio(matrix):
    N = len(matrix)
    if not all([matrix[i][i] == 0 for i in range(N)]):
        return False
    if not all([matrix[i][j] == -matrix[j][i] for i in range(N) for j in range(N)]):
        return False
    return True
