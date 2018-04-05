def double_substring(line):
    n = len(line)
    subs = [len(line[b:e+1]) for b in range(n) for e in range(b, n) if line.find(line[b:e+1], e+1) >= 0]
    return max(subs) if subs else 0
