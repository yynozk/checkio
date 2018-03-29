from datetime import datetime

def date_time(time):
    d = datetime.strptime(time, "%d.%m.%Y %H:%M")
    h = "hour" if d.hour == 1 else "hours"
    m = "minute" if d.minute == 1 else "minutes"
    return f"{d.day} {d.strftime('%B')} {d.year} year {d.hour} {h} {d.minute} {m}"
