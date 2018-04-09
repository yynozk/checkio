import datetime as dt

def broken_clock(starting_time, wrong_time, error_description):
    desc = error_description.split()
    gap = int(desc[0])
    gap = gap * 60 if "minute" in desc[1] else gap
    gap = gap * 60 * 60 if "hour" in desc[1] else gap
    per = int(desc[3])
    per = per * 60 if "minute" in desc[4] else per
    per = per * 60 * 60 if "hour" in desc[4] else per

    starting_time = dt.datetime.strptime(starting_time, "%H:%M:%S")
    wrong_time = dt.datetime.strptime(wrong_time, "%H:%M:%S")
    diff = wrong_time - starting_time

    right_progress = dt.timedelta(seconds=diff.seconds * (per / (gap + per)))
    return (starting_time + right_progress).strftime("%H:%M:%S")
