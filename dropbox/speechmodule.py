FIRST_TEN = ["one", "two", "three", "four", "five", "six", "seven",
             "eight", "nine"]
SECOND_TEN = ["ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen",
              "sixteen", "seventeen", "eighteen", "nineteen"]
OTHER_TENS = ["twenty", "thirty", "forty", "fifty", "sixty", "seventy",
              "eighty", "ninety"]
HUNDRED = "hundred"


def checkio(number):
    hundred = 0
    if number >= 100:
        hundred = number // 100
        number %= 100

    if number < 20:
        speech = ([""] + FIRST_TEN + SECOND_TEN)[number]
    elif number % 10 == 0:
        speech = OTHER_TENS[number // 10 - 2]
    else:
        t, o = [int(c) for c in str(number)]
        speech = f"{OTHER_TENS[t - 2]} {FIRST_TEN[o - 1]}"

    if hundred > 0:
        speech = f"{FIRST_TEN[hundred - 1]} {HUNDRED} {speech}"

    return speech.strip()
