from functools import reduce

day_9_input_path = '../../resources/day-9-input'

values_f = open(day_9_input_path, 'r')
values = [[int(y) for y in x.strip()] for x in values_f.readlines()]

print(f"{values}")

low_points = []


def is_low_point(i, j):
    val = values[i][j]
    print(f"Considering values[{i}][{j}] = {val}")

    left = (i-1 < 0 or val < values[i-1][j])
    up = (j-1 < 0 or val < values[i][j-1])
    right = (i >= len(values) - 1 or val < values[i+1][j])
    down = (j >= len(values[i]) - 1 or val < values[i][j+1])

    return left and up and right and down


for i in range(0, len(values)):
    row = values[i]
    for j in range(0, len(row)):
        if is_low_point(i, j):
            print(f"Appending {values[i][j]}")
            low_points.append(values[i][j])

print(low_points)
risk_levels = [x+1 for x in low_points]
print(f"Risk levels: {risk_levels}, sum: {reduce(int.__add__, risk_levels)}")