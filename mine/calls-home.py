from collections import defaultdict
import math

def total_cost(calls):
    used_minutes = defaultdict(int)
    for call in calls:
        d, _, s = call.split()
        used_minutes[d] += math.ceil(int(s) / 60)

    day_cost = lambda min: min if min <= 100 else 100 + (min - 100) * 2
    return sum([day_cost(s) for s in used_minutes.values()])
