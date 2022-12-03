day_1_input_path = '../../../resources/2022/day1-input'


values_f = open(day_1_input_path, 'r')
values = [x.strip() for x in values_f.readlines()]

print(f"{values}")

current_sum = 0
elves_list = []

for value in values:
    if len(value) == 0:
        elves_list.append(current_sum)
        current_sum = 0
    else:
        current_sum += int(value)

elves_list.sort()
elves_list.reverse()
print(f"Elves list is now {elves_list}, sum of top 3: {elves_list[0]+elves_list[1]+elves_list[2]}")

