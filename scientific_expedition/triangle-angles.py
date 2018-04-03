import math

def d(a, b, c):
    return round(math.degrees(math.acos((b*b + c*c - a*a) / (2*b*c))))

def checkio(a, b, c):
    return sorted([d(a,b,c), d(b,c,a), d(c,a,b)]) if a+b+c-max(a,b,c) > max(a,b,c) else [0,0,0]
