day_11_input_path = '../../resources/day-11-input'

values_f = open(day_11_input_path, 'r')
values = [[int(y) for y in x.strip()] for x in values_f.readlines()]

print(f"{values}")

STEPS = 800
flash_count = 0


def increment_all(values):
    for i in range(0, len(values)):
        for j in range(0, len(values[i])):
            values[i][j] += 1


def any_over_nine(values, flashed_ones):
    for i in range(0, len(values)):
        for j in range(0, len(values[i])):
            if values[i][j] > 9 and (i, j) not in flashed_ones:
                print("Yes! Im over nine!")
                return True
    return False


def increment_adjacents(values, i, j):
    if i > 0 and j > 0:
        values[i-1][j-1] += 1
    if i > 0:
        values[i-1][j] += 1
    if j > 0:
        values[i][j-1] += 1
    if i < len(values)-1:
        values[i+1][j] += 1
    if j < len(values[i]) -1:
        values[i][j+1] += 1
    if i < len(values)-1 and j < len(values[i]) -1:
        values[i+1][j+1] += 1
    if i > 0 and j < len(values[i]) - 1:
        values[i-1][j+1] += 1
    if i < len(values) - 1 and j > 0:
        values[i+1][j-1] += 1


def keep_on_flashing(values, flashed_ones):
    local_flash_count = 0
    # print("ITERATION OF FLASHING")
    for i in range(0, len(values)):
        for j in range(0, len(values[i])):
            if values[i][j] > 9 and (i, j) not in flashed_ones:
                # print(f"Imma flash {i}, {j}")
                increment_adjacents(values, i, j)
                local_flash_count += 1
                flashed_ones.add((i, j))
    # print(f"Added {local_flash_count} flashes")
    return local_flash_count


def zero_flashing_ones(values, flashed_ones):
    times_zeroed = 0
    for i, j in flashed_ones:
        values[i][j] = 0
        times_zeroed += 1
    return times_zeroed


def draw_board(board):
    for line in board:
        print(line)


def size(values):
    return len(values) * len(values[0])


for step in range(STEPS):
    print(f"Going with step {step}:")
    # draw_board(values)

    flashed_ones = set()
    increment_all(values)
    while any_over_nine(values, flashed_ones):
        flash_count += keep_on_flashing(values, flashed_ones)
    times_zeroed = zero_flashing_ones(values, flashed_ones)
    if times_zeroed == size(values):
        print(f"FOUND THE STEP WHERE IT ALL FLASHED AT THE SAME TIME: {step+1}")


print(f"Flashed {flash_count} times.")