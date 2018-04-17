from datetime import date

def checkio(year):
    return [date(year, i+1, 13).weekday() for i in range(12)].count(4)
