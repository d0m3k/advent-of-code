day_9_input_path = '../../../resources/2022/day9-input-example'

values_f = open(day_9_input_path, 'r')
lines = [x.strip().split(' ') for x in values_f.readlines()]

print(f"{lines}")

H, T = (0,0), (0,0)
been_there = set()

def go_in_direction(tuple, direction):
    a, b = tuple
    if direction == 'U':
        return (a+1), b
    if direction == 'R':
        return a, (b+1)
    if direction == 'L':
        return a, (b-1)
    if direction == 'D':
        return (a-1), b


def follow_if_needed(T, H):
    a, b = T
    i, j = H
    # fixme: remember about diagonal
    if abs(a-i) > 1: # you need to sprung in first dimention
        if a-i <0 :
            return a+1, b
        else:
            return a-1, b





for direction, count_s in lines:
    count = int(count_s)
    print(f"Going into {direction} {count} times")
    for i in range(count):
        H = go_in_direction(H, direction)
        print(H)
        T = follow_if_needed(T, H)
        been_there.add(T)