MAX = 2**16-1

def checkio(price, denominations):
    dp = [[0] for _ in denominations]

    for r, coin in enumerate(denominations):
        for c in range(1, price+1):
            vals = [MAX]
            if c >= coin: vals.append(dp[r][c-coin] + 1)
            if r > 0: vals.append(dp[r-1][c])
            dp[r].append(min(vals))

    return None if dp[-1][-1] == MAX else dp[-1][-1]
