def most_frequent(data):
    return max(data, key=lambda c: data.count(c))
