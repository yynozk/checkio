def largest_histogram(histogram):
    n = len(histogram)
    subs = [histogram[b:e] for b in range(n+1) for e in range(b+1, n+1)]
    return max(map(lambda a: min(a) * len(a), subs))
