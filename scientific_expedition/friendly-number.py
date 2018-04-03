import math

def friendly_number(number, base=1000, decimals=0, suffix='',
                    powers=['', 'k', 'M', 'G', 'T', 'P', 'E', 'Z', 'Y']):
    if number == 0:
        return f"{number:.{decimals}f}{suffix}"
    prefix = "-" if number < 0 else ""
    number = abs(number)
    p = min(math.floor(math.log(number, base)), len(powers)-1)
    n = math.floor(number / base**p) if decimals == 0 else round(number / base**p, decimals)
    return f"{prefix}{n:.{decimals}f}{powers[p]}{suffix}"
