def completely_empty(val):
    try:
        return all([completely_empty(e) for e in val])
    except:
        return False
