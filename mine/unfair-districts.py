import string

g_districts = []

def is_district(idxs, row, col):
    district = [idxs[0]]
    queue = [idxs[0]]
    while queue:
        nextto = []
        i = queue.pop()
        if i - col >= 0: nextto.append(i - col)
        if i + col < row * col: nextto.append(i + col)
        if i % col != col - 1: nextto.append(i + 1)
        if i % col != 0: nextto.append(i - 1)
        for n in nextto:
            if n in idxs and n not in district:
                district.append(n)
                queue.append(n)

    return sorted(idxs) == sorted(district)


def create_districts(idxs, now_index, amount, nums, grid):
    if now_index > len(nums):
        return

    if amount == 0:
        if is_district(idxs, len(grid), len(grid[0])):
            g_districts.append((set(idxs), comp_election(idxs, grid)))
        return

    for i in range(now_index, len(nums)):
        if nums[i] <= amount:
            create_districts(idxs + [i], i+1, amount-nums[i], nums, grid)


def comp_election(district, grid):
    COL = len(grid[0])

    a = b = 0
    for idx in district:
        a += grid[idx//COL][idx%COL][0]
        b += grid[idx//COL][idx%COL][1]

    if a > b:
        return 1
    elif a < b:
        return -1
    else:
        return 0


def is_answer(map, grid):
    COL = len(grid[0])

    win_a = win_b = 0
    for d in map:
        a = b = 0
        for idx in d:
            a += grid[idx//COL][idx%COL][0]
            b += grid[idx//COL][idx%COL][1]
        if a > b: win_a += 1
        if a < b: win_b += 1

    return win_a > win_b


def create_map(idxs, now_index, districts, grid):
    if sum([len(d[0]) for d in idxs]) == len(grid) * len(grid[0]):
        return idxs

    for i in range(now_index, len(districts)):
        if not ({i for d in idxs for i in d[0]} & districts[i][0]):
            map = create_map(idxs + [districts[i]], i+1, districts, grid)
            if map and sum([point for (_, point) in map]) > 0:
                return map

    return None


def unfair_districts(amount_of_people, grid):
    g_districts.clear()
    COL = len(grid[0])

    nums = [a + b for row in grid for (a, b) in row]
    create_districts([], 0, amount_of_people, nums, grid)

    map = create_map([], 0, g_districts, grid)
    if not map:
        return []
    ascii = string.ascii_uppercase[0:len(map)]

    ans = [["" for _ in grid[0]] for _ in grid]
    for (alphabet, district) in zip(ascii, [d for (d, _) in map]):
        for i in district:
            ans[i // COL][i % COL] = alphabet

    return ["".join(row) for row in ans]
