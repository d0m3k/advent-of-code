day_1_input_path = '../../../resources/2023/day1'


values_f = open(day_1_input_path, 'r')

sum_of_all = 0
for line in values_f.readlines():
    first, last = 0, 0
    for letter in line:
        if letter.isnumeric():
            if first == 0:
                first = int(letter)
            last = int(letter)
    print(f"in line got {first}{last}")
    sum_of_all = sum_of_all + int(f"{first}{last}")

print(f"Sum of all: {sum_of_all}")