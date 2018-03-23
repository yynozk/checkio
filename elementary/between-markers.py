import re

def between_markers(text: str, begin: str, end: str) -> str:
    if re.search(f"{re.escape(end)}.*{re.escape(begin)}", text):
        return ""
    return text.split(begin)[-1].split(end)[0]
