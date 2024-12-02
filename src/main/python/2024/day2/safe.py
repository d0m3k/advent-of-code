input_path = '../../../resources/2024/day2'

values_f = open(input_path, 'r')

result = 0

for report in values_f.readlines():
    levels = [int(x) for x in report.split()]
    should_add = True
    if levels[0] > levels[-1]:
        #         decreasing case
        for a, b in zip(levels, levels[1:]):
            if b > a or a - b == 0 or a - b > 3:
                should_add = False
                #     fixme probably should have a function in such case
    else:
        #         increasing case
        for a, b in zip(levels, levels[1:]):
            if a > b or b - a == 0 or b - a > 3:
                should_add = False
    if should_add:
        result = result + 1

print(f"Result: {result}")
