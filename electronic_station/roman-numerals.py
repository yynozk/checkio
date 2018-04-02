def checkio(data):
    symbols = [(1000, "M"), (500, "D"), (100, "C"), (50, "L"),(10, "X"), (5, "V"), (1, "I")]
    roman = []
    for n, c in symbols:
        while data - n >= 0:
            data -= n
            roman.append(c)

    return "".join(roman).replace("CCCC", "CD").replace("XXXX", "XL").replace("IIII", "IV")\
        .replace("DCD", "CM").replace("LXL", "XC").replace("VIV", "IX")
