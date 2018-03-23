def popular_words(text, words):
    text = text.lower()
    return dict(zip(words, map(lambda w: text.count(w), words)))
