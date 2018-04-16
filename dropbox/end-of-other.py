def checkio(words_set):
    reversed_words = [s[::-1] for s in words_set]
    while reversed_words:
        w1 = reversed_words.pop()
        for w2 in reversed_words:
            if w1.find(w2) == 0 or w2.find(w1) == 0:
                return True

    return False
