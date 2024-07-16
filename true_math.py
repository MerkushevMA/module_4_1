from math import inf

def divide(first, second):
    result = 0
    if second == 0:
        if first > 0:
            result = float(inf)
        elif first < 0:
            result = float(-inf)
    else:
        result = first / second
    return result
