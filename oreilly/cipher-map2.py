def pick(grille, password):
    return [password[r][c] for r in range(4) for c in range(4) if grille[r][c] == 'X']

def turn(square):
    return [[square[3-c][r] for c in range(4)] for r in range(4)]

def recall_password(cipher_grille, ciphered_password):
    password = []
    for _ in range(4):
        password.extend(pick(cipher_grille, ciphered_password))
        cipher_grille = turn(cipher_grille)

    return "".join(password)
