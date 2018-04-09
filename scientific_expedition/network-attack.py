from itertools import count

def capture(matrix):
    N = len(matrix)
    for min in count(1):
        infected = [i for i in range(N) if matrix[i][i] <= 0]
        attacked = {i for node in infected for i, conn in enumerate(matrix[node]) if conn == 1}
        for i in attacked:
            matrix[i][i] -= 1

        if all([matrix[i][i] <= 0 for i in range(N)]):
            return min
