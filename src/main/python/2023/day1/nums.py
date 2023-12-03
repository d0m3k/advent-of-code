day_1_input_path = '../../../resources/2023/day1'


values_f = open(day_1_input_path, 'r')

digits = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9
}

sum_of_all = 0


def number_or_literal_number(line, i):
    letter = line[i]

    if letter.isnumeric():
        return int(letter)

    alpha_number = None
    if line[i:i+3] in digits.keys():
        return digits[line[i:i+3]]
    if line[i:i+4] in digits.keys():
        return digits[line[i:i+4]]
    if line[i:i+5] in digits.keys():
        return digits[line[i:i+5]]
    return None


for line in values_f.readlines():
    first, last = 0, 0
    for i in range(0, len(line)):
        letter = line[i]
        maybe_number = number_or_literal_number(line, i)
        if maybe_number:
            if first == 0:
                first = maybe_number
            last = maybe_number

    print(f"in line got {first}{last}")
    sum_of_all = sum_of_all + int(f"{first}{last}")

print(f"Sum of all: {sum_of_all}")