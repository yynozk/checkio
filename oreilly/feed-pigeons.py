from itertools import count

def checkio(number):
    feed, pigeon = 0, 0
    for i in count(1):
        feed += pigeon + i
        pigeon += i

        if feed >= number:
            print(i, feed, number, pigeon)
            return pigeon - min(feed - number, i)
