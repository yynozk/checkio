from datetime import date, timedelta
from collections import Counter

WEEKDAYS = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

def most_frequent_days(year):
    cnt = Counter()

    begin, end = date(year, 1, 1), date(year+1, 1, 1)
    for i in range((end - begin).days):
        d = begin + timedelta(i)
        cnt[d.weekday()] += 1

    return [WEEKDAYS[w] for w, c in sorted(cnt.items()) if c == max(cnt.values())]
