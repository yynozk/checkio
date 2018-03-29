from itertools import count

def checkio(opacity):
    age = 10000
    fibo = (1, 1)
    for year in count(start=1):
        if age == opacity:
            return year - 1

        if year in fibo:
            age -= year
            fibo = (max(fibo), min(fibo) + max(fibo))
        else:
            age += 1
