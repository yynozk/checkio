import re

def long_repeat(line):
    return max(len(m.group()) for m in re.finditer(r'(.)\1*', line)) if line else 0
