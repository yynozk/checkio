def verify_anagrams(first_word, second_word):
    return sorted(first_word.lower().replace(" ", "")) == sorted(second_word.lower().replace(" ", ""))
