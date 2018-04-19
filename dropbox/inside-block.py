def is_inside(polygon, point):
    cross = 0
    for i in range(-1, len(polygon) - 1):
        beg, end = polygon[i], polygon[i+1]

        if min(beg[0],end[0]) <= point[0] <= max(beg[0],end[0]) \
            and min(beg[1],end[1]) <= point[1] <= max(beg[1],end[1]) \
            and (end[0]-beg[0])*(point[1]-beg[1]) == (end[1]-beg[1])*(point[0]-beg[0]):
            return True

        if beg[1] <= point[1] < end[1] or end[1] <= point[1] < beg[1]:
            v = (point[1] - beg[1]) / (end[1] - beg[1])
            if point[0] < beg[0] + (end[0] - beg[0]) * v:
                cross += 1

    return False if cross % 2 == 0 else True
