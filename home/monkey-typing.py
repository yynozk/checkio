def count_words(text, words):
    return sum(text.lower().find(w) >= 0 for w in words)
