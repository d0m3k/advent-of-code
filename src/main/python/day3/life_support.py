
day_3_input_path = '../../resources/day-3-input'

values_f = open(day_3_input_path, 'r')
values = values_f.readlines()

data_width = len(values[0])


# calculate oxygen
oxygen_values = values.copy()

oxygen_result = ''

for column in range(0, data_width-1):
    print("Column number {}".format(column))
    o_len = len(oxygen_values)

    if o_len == 0:
        break

    count_ones = 0

    for line in oxygen_values:
        current_val = line[column]
        if current_val == '1':
            count_ones += 1

    count_zeros = o_len - count_ones

    if count_ones >= count_zeros:
        chosen_number = '1'
    else:
        chosen_number = '0'

    oxygen_result += chosen_number
    oxygen_values = [line for line in oxygen_values if line[column] == chosen_number]
    print("Chosen number {}; Oxygen values now has len {}, values: {}; current res: {}".format(chosen_number, len(oxygen_values), oxygen_values, oxygen_result))

print("Oxygen result is {}, oxygen values: {}".format(oxygen_result, oxygen_values))

# calculate scrubber
