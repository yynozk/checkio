def decode_amsco(message, key):
    digits = [int(d) - 1 for d in str(key)]
    n = len(message)

    cipher_map = [[] for _ in range(len(digits))]
    while n > 0:
        for idx, d in enumerate(digits):
            length = (idx + len(cipher_map[d])) % 2 + 1
            cipher_map[d].append(min(length, n))
            n -= min(length, n)

    for r, row in enumerate(cipher_map):
        for c, length in enumerate(row):
            cipher_map[r][c] = message[0:length]
            message = message[length:]

    cipher_map = [e[1] for e in sorted(enumerate(cipher_map), key=lambda e: digits.index(e[0]))]
    cipher_map = list(map(list, zip(*cipher_map)))
    return "".join(["".join(r) for r in cipher_map])
