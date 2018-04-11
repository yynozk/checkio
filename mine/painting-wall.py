import copy

def checkio(required, operations):
    painted = []
    for nth, (ope_l, ope_r) in enumerate(operations, start=1):
        left, right = 0, 0
        for idx, (painted_l, _) in enumerate(painted):
            if painted_l <= ope_l:
                left = idx
            if painted_l <= ope_r:
                right = idx + 1

        new = copy.copy(painted[left:right])
        del painted[left:right]
        new.append((ope_l, ope_r))
        new.sort(key=lambda p: p[0])
        for i in range(1, len(new)):
            if new[i][0] <= new[i-1][1]:
                new[i] = (min(new[i-1][0], new[i][0]), max(new[i-1][1], new[i][1]))
                new[i-1] = None

        painted.extend([r for r in new if r])
        painted.sort(key=lambda p: p[0])
        if sum([r - new + 1 for (new, r) in painted]) >= required:
            return nth

    return -1
