from typing import List, Any

def all_the_same(elements: List[Any]) -> bool:
    if len(elements) < 2:
        return True
    for e in elements:
        if e != elements[0]:
            return False
    return True
