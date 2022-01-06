day_8_input_path = '../../resources/day-8-input-short'

values_f = open(day_8_input_path, 'r')
values = [x.strip().split(' | ') for x in values_f.readlines()]


outputs = [x[1] for x in values]

print(f"{outputs}")

length_map = {}
for output in outputs:
    for word in output.split(' '):
        if not length_map.get(len(word)):
            length_map[len(word)] = 0
        length_map[len(word)] += 1

print(f"{length_map}")

print(f"{length_map[2] + length_map[4] + length_map[3] + length_map[7]}")
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

# TODO: below is fully WIP

# TODO: you will probably want to sort signals to make sure you get the same left-right
def decode_digits(lr):
    signals, outputs = lr[0], lr[1]

    return output


for value in values:
    print(decode_digits(value))