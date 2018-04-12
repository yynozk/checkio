def find_enemy(you, dir, enemy):
    vx, vy = ord(enemy[0]) - ord(you[0]), (int(enemy[1]) - int(you[1])) * 2
    if (vx + vy) % 2 != 0:
        vy += 1 if vy > 0 else -1

    if vx == 0:
        enemy_dir = "S" if vy > 0 else "N"
    elif abs(vx) == abs(vy):
        if vx > 0 and vy > 0: enemy_dir = "SE"
        if vx > 0 and vy < 0: enemy_dir = "NE"
        if vx < 0 and vy > 0: enemy_dir = "SW"
        if vx < 0 and vy < 0: enemy_dir = "NW"
    elif -abs(vx) <= vy <= abs(vx):
        enemy_dir = "E" if vx > 0 else "W"
    else:
        if vx > 0 and vy > 0: enemy_dir = "SSE"
        if vx > 0 and vy < 0: enemy_dir = "NNE"
        if vx < 0 and vy > 0: enemy_dir = "SSW"
        if vx < 0 and vy < 0: enemy_dir = "NNW"

    DIRS = ["N", "NE", "SE", "S", "SW", "NW"]
    rotate_count = DIRS.index(dir)

    ENEMY_DIRS = ["N", "NNE", "NE", "E", "SE", "SSE", "S", "SSW", "SW", "W", "NW", "NNW"]
    RELATIVE_DIRS = ["F", "F", "R", "R", "R", "B", "B", "B", "L", "L", "L", "F"]
    reldir_index = (ENEMY_DIRS.index(enemy_dir) - rotate_count*2) % len(RELATIVE_DIRS)
    reldir = RELATIVE_DIRS[reldir_index]

    vx, vy = abs(vx), abs(vy)
    xymin = min(vx, vy)
    distance = xymin + (vx - xymin) + (vy - xymin)//2

    return [reldir, distance]
