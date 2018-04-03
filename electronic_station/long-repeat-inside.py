def repeat_inside(line):
    n = len(line)
    subs = [line[b:e] for b in range(n+1) for e in range(b+1, n+1) if len(line[b:e]) >= 2]
    subs = list(filter(lambda s: len(s) == s.count(s[0]) or s[:len(s)//2] == s[len(s)//2:], subs))
    return max(subs, key=len) if subs else ""
