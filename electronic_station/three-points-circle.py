import math
import re

def checkio(data):
    x1, y1, x2, y2, x3, y3 = map(int, data.replace("(", "").replace(")", "").split(","))

    a11 = 2 * (x2 - x1)
    a12 = 2 * (y2 - y1)
    a21 = 2 * (x3 - x2)
    a22 = 2 * (y3 - y2)
    b11 = x2**2 + y2**2 - x1**2 - y1**2
    b21 = x3**2 + y3**2 - x2**2 - y2**2
    datA = a11 * a22 - a12 * a21
    A = [[a22 / datA, -a12 / datA],
         [-a21 / datA, a11 / datA]]
    B = [[b11],
         [b21]]
    x0 = A[0][0] * B[0][0] + A[0][1] * B[1][0]
    y0 = A[1][0] * B[0][0] + A[1][1] * B[1][0]
    r =  math.sqrt((x1 - x0)**2 + (y1 - y0)**2)

    x0s = re.sub(r"\.?0*$", "", str(round(x0, 2)))
    y0s = re.sub(r"\.?0*$", "", str(round(y0, 2)))
    rs = re.sub(r"\.?0*$", "", str(round(r, 2)))
    return f"(x-{x0s})^2+(y-{y0s})^2={rs}^2"
