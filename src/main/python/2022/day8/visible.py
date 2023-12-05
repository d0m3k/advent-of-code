day_8_input_path = '../../../resources/2022/day8-input-example'


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
        max_height = -1
        for j in inner_iterator:
            if int(lines[i][j]) > max_height:
                max_height = int(lines[i][j])
                result.add((i, j))
    return result


def iterate_and_add_vertical(lines, outer_iterator, inner_iterator):
    print(f"Iterating with {outer_iterator}; {inner_iterator}")
    result = set()
    for j in outer_iterator:
        max_height = -1
        for i in inner_iterator:
            if int(lines[i][j]) > max_height:
                max_height = int(lines[i][j])
                result.add((i, j))
    return result


can_be_seen.update(iterate_and_add_horizontal(lines, range(WIDTH), range(HEIGHT)))
can_be_seen.update(iterate_and_add_horizontal(lines, range(WIDTH), range(HEIGHT-1, -1, -1)))
can_be_seen.update(iterate_and_add_vertical(lines, range(WIDTH), range(HEIGHT)))
can_be_seen.update(iterate_and_add_vertical(lines, range(WIDTH), range(HEIGHT-1, -1, -1)))

print(f"Part 1: There are {len(can_be_seen)} visible trees: {can_be_seen}")

# max score should be that you can see most of the trees outside of some point
# so this is the same algorithm, but... you would need to set ranges for all the trees, if done naively
# would naive solution be enough?

scores = {}
highest_scenic_score = 0

# for each tree, use iterate_and_add, but only for single row and starting "from it"
for i in range(WIDTH):
    for j in range(HEIGHT):
        print(f"\nLooking at tree with height {lines[i][j]}, ({i},{j})")
        scenic_score = len(iterate_and_add_horizontal(lines, [i], range(j+1, HEIGHT)))
        scenic_score *= len(iterate_and_add_horizontal(lines, [i], range(j-1, -1, -1)))
        scenic_score *= len(iterate_and_add_vertical(lines, [j], range(i+1, HEIGHT)))
        scenic_score *= len(iterate_and_add_vertical(lines, [j], range(i-1, -1, -1)))

        scores[(i,j)] = scenic_score
        if scenic_score > highest_scenic_score:
            highest_scenic_score = scenic_score

print(f"Scores: {scores}, highest: {highest_scenic_score}")


