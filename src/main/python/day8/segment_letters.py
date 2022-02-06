day_8_input_path = '../../resources/day-8-input'

values_f = open(day_8_input_path, 'r')
values = [x.strip().split(' | ') for x in values_f.readlines()]


# length_map = {}
# for output in outputs:
#     for word in output.split(' '):
#         if not length_map.get(len(word)):
#             length_map[len(word)] = 0
#         length_map[len(word)] += 1
#
# print(f"{length_map}")
#
# print(f"{length_map[2] + length_map[4] + length_map[3] + length_map[7]}")
#  1: 2 segments
#  2: 5 segments
#  3: 5 segments
#  4: 4 segments
#  5: 5 segments
#  6: 6 segments
#  7: 3 segments
#  8: 7 segments
#  9: 6 segments
#  0: 6 segments

# so:
# 2s: 1
# 3s: 7
# 4s: 4
# 5s: 2,3,5
# 6s: 6,9,0
# 7s: 8

# non uniques:
# 2: have 1 common with 1, 2 common with 7, 2 common with 4, 5 common with 8
# 3: have 2 common with 1, 3 common with 7, 3 common with 4, 5 common with 8
# 5: have 1 common with 1, 2 common with 7, 3 common with 4, 5 common with 8

# 6: have 1 common with 1, 2 common with 7, 3 common with 4, 6 common with 8
# 9: have 2 common with 1, 3 common with 7, 4 common with 4, 6 common with 8
# 0: have 2 common with 1, 3 common with 7, 3 common with 4, 6 common with 8

# TODO: below is fully WIP

def common(list1, list2):
    if not list2:
        # print("Dunno yet *shrug*")
        return
    return len(list(set(list1).intersection(list2)))


# TODO: you will probably want to sort signals to make sure you get the same left-right
def decode(signal, result_map, sg):
    if len(signal) == 2:
        result_map[1] = sg
    elif len(signal) == 3:
        result_map[7] = sg
    elif len(signal) == 4:
        result_map[4] = sg
    elif len(signal) == 7:
        result_map[8] = sg
    elif len(signal) == 5:
        # 2: have 1 common with 1, 2 common with 7, 2 common with 4, 5 common with 8
        # 3: have 2 common with 1, 3 common with 7, 3 common with 4, 5 common with 8
        # 5: have 1 common with 1, 2 common with 7, 3 common with 4, 5 common with 8
        if common(sg, result_map[1]) == 1 and common(sg, result_map[7]) == 2 and common(sg, result_map[4]) == 2:
            result_map[2] = sg
        elif common(sg, result_map[1]) == 2 and common(sg, result_map[7]) == 3 and common(sg, result_map[4]) == 3:
            result_map[3] = sg
        elif common(sg, result_map[1]) == 1 and common(sg, result_map[7]) == 2 and common(sg, result_map[4]) == 3:
            result_map[5] = sg
    elif len(signal) == 6:
        # 6: have 1 common with 1, 2 common with 7, 3 common with 4, 6 common with 8
        # 9: have 2 common with 1, 3 common with 7, 4 common with 4, 6 common with 8
        # 0: have 2 common with 1, 3 common with 7, 3 common with 4, 6 common with 8
        if common(sg, result_map[1]) == 1 and common(sg, result_map[7]) == 2 and common(sg, result_map[4]) == 3:
            result_map[6] = sg
        elif common(sg, result_map[1]) == 2 and common(sg, result_map[7]) == 3 and common(sg, result_map[4]) == 4:
            result_map[9] = sg
        elif common(sg, result_map[1]) == 2 and common(sg, result_map[7]) == 3 and common(sg, result_map[4]) == 3:
            result_map[0] = sg


def read_values(result_map, outputs):
    outputs_as_strings = ["".join(x) for x in outputs]
    inverse_map = {"".join(vals): key for key, vals in result_map.items()}
    # print(f"Going with {outputs_as_strings} / {inverse_map}")
    return "".join([str(inverse_map[x]) for x in outputs_as_strings])


def decode_digits(lr):
    signals, outputs = lr[0].split(' '), lr[1].split(' ')
    signals = [sorted(x) for x in signals]
    outputs = [sorted(x) for x in outputs]
    # print(f"{signals} / {outputs}")

    result_map = {
        0: [],
        1: [],
        2: [],
        3: [],
        4: [],
        5: [],
        6: [],
        7: [],
        8: [],
        9: []
    }
    for signal in signals:
        decode("".join(signal), result_map, signal)
    # print(f"After first loop: {result_map}")
    for signal in signals:
        decode("".join(signal), result_map, signal)
    # print(f"After second loop: {result_map}")
    result_for_line = read_values(result_map, outputs)
    print(f"Result for line: {result_for_line}")
    return int(result_for_line)


sum = 0

for value in values:
    sum += decode_digits(value)

print(f"Final sum: {sum}")