import re

def second_index(text: str, symbol: str):
    idx = re.sub(symbol, chr(ord(symbol)+1), text, 1).find(symbol)
    return idx if idx >= 0 else None
