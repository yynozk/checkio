def morse(c):
    return c if c == ":" else f"{int(c):04b}".translate(str.maketrans("01", ".-"))

def checkio(time_string):
    time_string = ":".join([s.zfill(2) for s in time_string.split(":")])
    ans = [morse(s) for s in time_string]
    ans[0] = ans[0][-2:]
    ans[3] = ans[3][-3:]
    ans[6] = ans[6][-3:]
    return " ".join(ans)
