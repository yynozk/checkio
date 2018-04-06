import re

VOWELS = "AEIOUY"
CONSONANTS = "BCDFGHJKLMNPQRSTVWXZ"

def isStripe(word):
    if len(word) <= 1:
        return False
    word = word.upper()
    pair = [VOWELS, CONSONANTS]
    if word[0] in VOWELS:
        idx = 0
    elif word[0] in CONSONANTS:
        idx = 1
    else:
        return False

    for c in word.upper():
        if c not in pair[idx]:
            return False
        idx = abs(idx - 1)

    return True


def checkio(text):
    return sum([1 for word in re.split("\W", text) if isStripe(word)])
