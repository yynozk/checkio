def left_join(phrases):
    return ",".join(map(lambda w: w.replace("right", "left"), phrases))
