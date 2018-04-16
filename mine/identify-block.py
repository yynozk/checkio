KINDS = {
    "I": [{1,2,3,4}, {1,5,9,13}],
    "J": [{2,6,9,10}, {1,5,6,7}, {1,2,5,9}, {1,2,3,7}],
    "L": [{1,5,9,10}, {1,2,3,5}, {1,2,6,10}, {3,5,6,7}],
    "O": [{1,2,5,6}],
    "S": [{2,3,5,6}, {1,5,6,10}],
    "T": [{1,2,3,6}, {2,5,6,10}, {2,5,6,7}, {1,5,6,9}],
    "Z": [{1,2,6,7}, {2,5,6,9}],
}

def identify_block(numbers):
    while not ({1,5,9,13} & numbers):
        numbers = {i - 1 for i in numbers}
    while not ({1,2,3,4} & numbers):
        numbers = {i - 4 for i in numbers}

    for kind, list in KINDS.items():
        if numbers in list:
            return kind
