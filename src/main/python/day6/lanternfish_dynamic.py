import itertools
from functools import reduce
from time import gmtime, strftime

day_6_input_path = '../../resources/day-6-input'

values_f = open(day_6_input_path, 'r')
fish_table = [int(x) for x in values_f.readline().split(',')]

DAYS = 256


# dyyynamic programming.
#Let us have a table of [fish (day of cycle)][days]
res_table = [[] for _ in range(0, 9)]
for i in range(0, len(res_table)):
    res_table[i] = [0 for _ in range(0, DAYS + 1)]

print(f"{res_table}")


# for each fish and day pair you can get the following:
# if fish starting from N days had X


# differenciate well two things:
# how many fish is born from a single fish. This is unbound.
# in which day of your cycle you are as a fish. This is upper bound by 8.

# go with the same solution as in lanternfish_recursive, but memoize things in between recursion...
def how_much_is_the(cycle_day, days):
    if days == 0:
        return 1
    # ... and read them when needed
    elif res_table[cycle_day][days] > 0:
        return res_table[cycle_day][days]
    elif cycle_day == 0:
        res_table[cycle_day][days] = how_much_is_the(8, days-1) + how_much_is_the(6, days-1)
        return res_table[cycle_day][days]
        # slight optimisation: if you are lively fish, drop some days immediately
    elif days > cycle_day:
        res_table[cycle_day][days] = how_much_is_the(0, days - cycle_day)
        return res_table[cycle_day][days]
    else:
        res_table[cycle_day][days] = how_much_is_the(cycle_day - 1, days - 1)
        return res_table[cycle_day][days]


fish_result = [how_much_is_the(fish, DAYS) for fish in fish_table]

print(f"{fish_result}, sum {reduce(int.__add__, fish_result)}")

