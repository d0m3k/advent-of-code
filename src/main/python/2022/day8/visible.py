day_8_input_path = '../../../resources/2022/day8-input'


values_f = open(day_8_input_path, 'r')
lines = [x.strip() for x in values_f.readlines()]
WIDTH = len(lines[0])
HEIGHT = len(lines)

print(f"{WIDTH}x{HEIGHT}")

# don't go over each tree and try to match if it's seen by "raying" from it;
# rather, go through lines four sides (x N) and add to set of seen trees, if seen

can_be_seen = set()

# iterate left to right:


def iterate_and_add_horizontal(lines, outer_iterator, inner_iterator):
    print(f"Iterating with {outer_iterator}; {inner_iterator}")
    result = set()
    for i in outer_iterator:
        print(f"Now in line {i}")
        max_height = -1
        for j in inner_iterator:
            if int(lines[i][j]) > max_height:
                print(f"Got height {lines[i][j]}, higher than {max_height} - adding ({i},{j})")
                max_height = int(lines[i][j])
                result.add((i, j))
    return result


def iterate_and_add_vertical(lines, outer_iterator, inner_iterator):
    print(f"Iterating with {outer_iterator}; {inner_iterator}")
    result = set()
    for j in outer_iterator:
        print(f"Now in column {j}")
        max_height = -1
        for i in inner_iterator:
            print(f"Now in row {i}")
            if int(lines[i][j]) > max_height:
                print(f"Got height {lines[i][j]}, higher than {max_height} - adding ({i},{j})")
                max_height = int(lines[i][j])
                result.add((i, j))
    return result


can_be_seen.update(iterate_and_add_horizontal(lines, range(WIDTH), range(HEIGHT)))
can_be_seen.update(iterate_and_add_horizontal(lines, range(WIDTH), range(HEIGHT-1, -1, -1)))
can_be_seen.update(iterate_and_add_vertical(lines, range(WIDTH), range(HEIGHT)))
can_be_seen.update(iterate_and_add_vertical(lines, range(WIDTH), range(HEIGHT-1, -1, -1)))


print(f"There are {len(can_be_seen)} visible trees: {can_be_seen}")
