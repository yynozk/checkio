def win(line):
    if line.count(line[0]) == 3:
        return line[0]
    return "."

def checkio(game_result):
    for row in game_result:
        line_res = win(row)
        if line_res != ".":
            return line_res

    for c in range(3):
        col = [game_result[r][c] for r in range(3)]
        line_res = win(col)
        if line_res != ".":
            return line_res

    diagonal1 = [game_result[i][i] for i in range(3)]
    line_res = win(diagonal1)
    if line_res != ".":
        return line_res

    diagonal2 = [game_result[i][2-i] for i in range(3)]
    line_res = win(diagonal2)
    if line_res != ".":
        return line_res

    return "D"
