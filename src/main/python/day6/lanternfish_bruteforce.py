day_6_input_path = '../../resources/day-6-input-short'

values_f = open(day_6_input_path, 'r')
fish_table = [int(x) for x in values_f.readline().split(',')]

DAYS = 256


def tick_a_fish(fish_index):
    if fish_table[fish_index] == 0:
        fish_table[fish_index] = 6
        fish_table.append(8)
    else:
        fish_table[fish_index] -= 1


print(f"Initial state: {fish_table}")

for d in range(1, DAYS+1):
    for fish_index in range(0, len(fish_table)):
        tick_a_fish(fish_index)
    if d % 10 == 0:
        print(f"At day {d}, current fish count: {len(fish_table)}")


print(f"Fish count: {len(fish_table)}")

# this does well in case up to ~190 days, but no more. Looking for function, then
