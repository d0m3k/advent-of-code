day_6_input_path = '../../../resources/2022/day6-input-example'


values_f = open(day_6_input_path, 'r')
signal = values_f.readline()

# just change this for part 1
EXPECTED_LEN = 14
already_found = []

for i in range(len(signal)):
    sign = signal[i]
    if len(already_found) >= EXPECTED_LEN:
        if len(already_found) == len(set(already_found)):
            print(f"Got ya! We got here at sign {i}")
            break
        already_found.pop(0)
    already_found.append(sign)
    print(f"Current already found: {already_found}")