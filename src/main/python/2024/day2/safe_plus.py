input_path = '../../../resources/2024/day2'

values_f = open(input_path, 'r')

result = 0

def check_decreasing(levels, dampener_used = False):
    for i in range(len(levels)-1):
        a,b = levels[i], levels[i+1]
        if b > a or a - b == 0 or a - b > 3:
            if not dampener_used:
                return check_level(levels[:i] + levels[i+1:], True) or check_level(levels[:i+1] + levels[i+2:], True)
            return False
    return True

def check_increasing(levels, dampener_used = False):
    for i in range(len(levels)-1):
        a,b = levels[i], levels[i+1]
        if a > b or b - a == 0 or b - a > 3:
            if not dampener_used:
                return check_level(levels[:i] + levels[i+1:], True) or check_level(levels[:i+1] + levels[i+2:], True)
            return False
    return True


def check_level(levels, dampener_used = False):
    if levels[0] > levels[-1]:
        #         decreasing case
        if check_decreasing(levels, dampener_used):
            print(f"Level {levels} is safe")
            return True
    else:
        if check_increasing(levels, dampener_used):
            print(f"Level {levels} is safe")
            return True
    return False


for report in values_f.readlines():
    levels = [int(x) for x in report.split()]
    result += check_level(levels)


print(f"Result: {result}")
