from functools import reduce
from time import gmtime, strftime

day_6_input_path = '../../resources/day-6-input-short'

values_f = open(day_6_input_path, 'r')
fish_table = [int(x) for x in values_f.readline().split(',')]

DAYS = 80


def how_much_is_the(fish, days):
    if days == 0:
        return 1
    elif fish == 0:
        return how_much_is_the(8, days-1) + how_much_is_the(6, days-1)
# slight optimisation: if you are lively fish, drop some days immediately
    elif days > fish:
        return how_much_is_the(0, days-fish)
    else:
        return how_much_is_the(fish-1, days-1)


# if you successfuly calculate one fish result, you can just reuse the same result for any fish starting with the same number

# even more: if you EVER calculate the same fish_days relation, you can reuse it

fish_result = []
for i in range(0, len(fish_table)):
    print(f'{strftime("%H:%M:%S", gmtime())} Calculating {i} fish...')
    fish_result.append(how_much_is_the(fish_table[i], DAYS))

# fish_result = [how_much_is_the(fish, DAYS) for fish in fish_table]

print(f"{fish_result}, sum {reduce(int.__add__, fish_result)}")