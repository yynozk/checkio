def reverse_roman(roman_string):
    symbols = [(1000, "M"), (500, "D"), (100, "C"), (50, "L"),(10, "X"), (5, "V"), (1, "I")]
    roman_string = roman_string.replace("CM", "DCD").replace("XC", "LXL").replace("IX", "VIV")\
        .replace("CD", "CCCC").replace("XL", "XXXX").replace("IV", "IIII")
    return sum([s[0] * roman_string.count(s[1]) for s in symbols])
