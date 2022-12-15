from functools import reduce

day_10_input_path = '../../../resources/y2021/day-10-input'

values_f = open(day_10_input_path, 'r')
values = [x.strip() for x in values_f.readlines()]

open_close = {
    '[': ']',
    '(': ')',
    '{': '}',
    '<': '>'
}

illegals = []
illegal_lines = []

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
                illegal_lines.append(line)


points = {
    ')': 3,
    ']': 57,
    '}': 1197,
    '>': 25137
}

cal_points = reduce(int.__add__, [points[x] for x in illegals])

print(f"Illegals: {illegals}, points: {cal_points}")

for line in illegal_lines:
    values.remove(line)

print(f"Lines left: {values}")

closer_points = {
    ')': 1,
    ']': 2,
    '}': 3,
    '>': 4
}

closer_results = []

for line in values:
    stack = []
    for char in line:
        if char in {'[', '(', '{', '<'}:
            stack.append(char)
        if char in {']', ')', '}', '>'}:
            to_close = stack.pop()
    print(f"For {line} left with stack: {stack}")
    closing = []
    while not len(stack) == 0:
        char = stack.pop()
        closing.append(open_close[char])
    print("Closers:" + "".join(closing))

    line_result = 0
    for closer in closing:
        line_result = 5 * line_result + closer_points[closer]
    closer_results.append(line_result)

print(f"Results for closers: {closer_results}")
closer_results.sort()
print(f"Middle element: {closer_results[len(closer_results)//2]}")