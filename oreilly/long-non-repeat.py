def non_repeat(line):
    n = len(line)
    return max([line[b:e] for b in range(n) for e in range(b+1, n+1) if len(set(line[b:e])) == e-b] + [""], key=len)
