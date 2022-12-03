
day_2_input_path = '../../../resources/2022/day2-input'


values_f = open(day_2_input_path, 'r')
values = [x.strip().split(' ') for x in values_f.readlines()]

print(f"{values}")

def first_iteration(values):
    result_sum = 0

    for o, y in values:
        if   y == 'X':
            result_sum += 1
            if   o == 'A':
                result_sum += 3
            elif o == 'B':
                result_sum += 0
            elif o == 'C':
                result_sum += 6
        elif y == 'Y':
            result_sum += 2
            if   o == 'A':
                result_sum += 6
            elif o == 'B':
                result_sum += 3
            elif o == 'C':
                result_sum += 0
        elif y == 'Z':
            result_sum += 3
            if   o == 'A':
                result_sum += 0
            elif o == 'B':
                result_sum += 6
            elif o == 'C':
                result_sum += 3

    print(f"Result 1 is {result_sum}")


def second_iteration(values):
    result_sum = 0

    for o, y in values:
        if   y == 'X': # lose
            result_sum += 0
            if   o == 'A':
                result_sum += 3
            elif o == 'B':
                result_sum += 1
            elif o == 'C':
                result_sum += 2
        elif y == 'Y': #draw
            result_sum += 3
            if   o == 'A':
                result_sum += 1
            elif o == 'B':
                result_sum += 2
            elif o == 'C':
                result_sum += 3
        elif y == 'Z': #win
            result_sum += 6
            if   o == 'A':
                result_sum += 2
            elif o == 'B':
                result_sum += 3
            elif o == 'C':
                result_sum += 1


    print(f"Result 2 is {result_sum}")


first_iteration(values)
second_iteration(values)
