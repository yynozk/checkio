import re

lower = re.compile(r".*[a-z]")
upper = re.compile(r".*[A-Z]")
number = re.compile(r".*[0-9]")

def checkio(data):
    if len(data) < 10:
        return False
    if not lower.match(data):
        return False
    if not upper.match(data):
        return False
    if not number.match(data):
        return False

    return True

#Some hints
#Just check all conditions


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio('A1213pokl') == False, "1st example"
    assert checkio('bAse730onE4') == True, "2nd example"
    assert checkio('asasasasasasasaas') == False, "3rd example"
    assert checkio('QWERTYqwerty') == False, "4th example"
    assert checkio('123456123456') == False, "5th example"
    assert checkio('QwErTy911poqqqq') == True, "6th example"
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")
