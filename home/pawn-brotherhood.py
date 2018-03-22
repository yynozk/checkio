def defense_pawn(place):
    pawns = set()
    c, r = place[0], int(place[1])
    if c > 'a' and r > 1:
        pawns.add(f"{chr(ord(c) - 1)}{r - 1}")
    if c < 'h' and r > 1:
        pawns.add(f"{chr(ord(c) + 1)}{r - 1}")
    return pawns

def safe_pawns(pawns):
    return sum(1 for p in pawns if len(pawns & defense_pawn(p)) > 0)
