day_7_input_path = '../../../resources/y2021/day-7-input'

values_f = open(day_7_input_path, 'r')
crab_table = [int(x) for x in values_f.readline().split(',')]

print(f"{crab_table}")

max_position = max(crab_table)
current_cheapest_position=(-1,1e16)


def arith(n):
    if n < 2:
        return n
    return n * (1+n)/2


for current_position_number in range(0, max_position+1):
    current_position_fuel = 0
    for crab in crab_table:
        # to get back to solution to first part, just don't wrap abs with arith
        current_position_fuel += arith(abs(crab-current_position_number))
    if current_position_fuel < current_cheapest_position[1]:
        current_cheapest_position = current_position_number, current_position_fuel

print(f"It turns out the optimal position is {current_cheapest_position[0]}, and it costs {current_cheapest_position[1]} fuel.")
