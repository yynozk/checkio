import re

def checkio(words):
    return True if re.search(r"\D+ \D+ \D+", words) else False
