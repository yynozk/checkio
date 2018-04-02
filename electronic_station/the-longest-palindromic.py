def longest_palindromic(text):
    return max([text[b:e] for b in range(len(text)+1) for e in range(b+1, len(text)+1) if text.find(text[b:e][::-1]) != -1], key=len)
