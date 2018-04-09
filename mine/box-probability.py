from collections import defaultdict

def checkio(marbles, step):
    swap = str.maketrans("bw", "wb")

    pattern_counts = {"".join(sorted(marbles)): 1}
    for i in range(step - 1):
        next_pattern_counts = defaultdict(int)
        for marbles, count in pattern_counts.items():
            for i in range(len(marbles)):
                swapped = marbles[:i] + marbles[i].translate(swap) + marbles[i+1:]
                next_pattern_counts["".join(sorted(swapped))] += count
        pattern_counts = next_pattern_counts

    w_count = sum([marbles.count("w") * count for marbles, count in pattern_counts.items()])
    return round(w_count / len(marbles)**(step), 2)
