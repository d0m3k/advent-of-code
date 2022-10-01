day_14_input_path = '../../resources/day-14-input'


values_f = open(day_14_input_path, 'r')
values = values_f.readlines()


def g_key(v):
    return v.strip().split(' -> ')[0]


def g_value(v):
    return v.strip().split(' -> ')[1]


polymer = values[0].strip()
growths = {g_key(values[x]): g_value(values[x]) for x in range(2, len(values))}

print(f'{growths}, {polymer}')

ITERATIONS = 40
print()
print(f"Template:\t\t{polymer}")

for i in range(1, ITERATIONS+1):
    new_polymer = ''
    for j in range(len(polymer)-1):
        current_pair = polymer[j] + polymer[j+1]
        to_add = growths[current_pair]
        new_polymer += current_pair[0] + to_add
    # edge case: add last one, as we "shift" only left above
    new_polymer += polymer[len(polymer)-1]
    polymer = new_polymer
    print(f"After step {i}:\twe have length {len(polymer)}")


def count_letters(string):
    letters = set(string)
    return {letter: string.count(letter) for letter in letters}


values_counts = count_letters(polymer)
print(values_counts)
most_common_count = max(values_counts.values())
least_common_count = min(values_counts.values())

print(f"Most common: {most_common_count}, min common: {least_common_count}, diff: {most_common_count-least_common_count}")