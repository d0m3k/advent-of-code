
day_3_input_path = '../../resources/day-3-input'

values_f = open(day_3_input_path, 'r')
values = values_f.readlines()

data_width = len(values[0])


def calculate_for(name, values, comparator):
    # calculate oxygen
    calc_values = values.copy()

    calc_result = ''

    for column in range(0, data_width):
        print("Column number {}".format(column))
        o_len = len(calc_values)

        if o_len == 1:
            break

        count_ones = 0

        for line in calc_values:
            current_val = line[column]
            if current_val == '1':
                count_ones += 1

        count_zeros = o_len - count_ones

        if comparator(count_ones, count_zeros):
            chosen_number = '1'
        else:
            chosen_number = '0'

        calc_result += chosen_number
        calc_values = [line for line in calc_values if line[column] == chosen_number]
        print("Chosen number {}; {} values now has len {}, values: {}; current res: {}".format(chosen_number, name, len(calc_values), calc_values, calc_result))

    result = calc_values[0]
    print("Result is what is left as last value, and that is {} (dec: {})".format(result, int(result, 2)))
    return int(result, 2)
    # written record of my original misunderstanding of what we are looking for (similarly to first part of today)
    # print("{} result is {} (dec: {}), values: {}".format(name, calc_result, int(calc_result, 2), calc_values))
    # return int(calc_result, 2)


dec_oxygen = calculate_for('Oxygen', values, (lambda ones, zeros: ones >= zeros))
dec_scrubber = calculate_for('Scrubber', values, (lambda ones, zeros: ones < zeros))
# 010110010011 / 1427

# calculate scrubber
print("Final result: {}".format(dec_oxygen * dec_scrubber))
