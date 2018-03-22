def checkio(data):
    ans = []
    for i in data:
        if data.count(i) > 1:
            ans.append(i)
    return ans
