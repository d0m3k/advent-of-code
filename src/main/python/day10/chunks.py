from functools import reduce

day_10_input_path = '../../resources/day-10-input'

values_f = open(day_10_input_path, 'r')
values = [x for x in values_f.readlines()]

open_close = {
    '[': ']',
    '(': ')',
    '{': '}',
    '<': '>'
}

illegals = []

for line in values:
    stack = []
    for char in line:
        if char in {'[', '(', '{', '<'}:
            stack.append(char)
        if char in {']', ')', '}', '>'}:
            to_close = stack.pop()
            if open_close[to_close] is not char:
                print(f"Illegal character '{char}' for line: {line}")
                illegals.append(char)

points = {
    ')': 3,
    ']': 57,
    '}': 1197,
    '>': 25137
}

cal_points = reduce(int.__add__, [points[x] for x in illegals])

print(f"Illegals: {illegals}, points: {cal_points}")
