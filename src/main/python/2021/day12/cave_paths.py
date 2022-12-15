day_12_input_path = '../../../resources/y2021/day-12-input'


def get_path_tuple(line):
    pair = line.split('-')
    return pair[0].strip(), pair[1].strip()

# this hacky, but working way makes the traverse algorithm work without considering direction
# note that 'end' is also being reversed here, so that we can get into
# the case where it is current_point (always terminating)
def add_reverse_tuples(tuples):
    additional_tuples = []
    for a, b in tuples:
        if a != 'start':
            additional_tuples.append((b, a))
    return additional_tuples


values_f = open(day_12_input_path, 'r')
values = values_f.readlines()

tuples = [get_path_tuple(x) for x in values]
tuples += add_reverse_tuples(tuples)
print(f"{tuples}")

found_paths = set()


def is_small_cave(name):
    return name.islower() and name != 'start' and name != 'end'


# start going into it by finding all start ones
# then, recursively get inside
# the stop params are re-entering already visited small cave (return 0), or visiting 'end' (return 1)
def traverse_cave(current_point, next_point, already_visited, special_chance):
    new_visited = already_visited.copy()
    # print(f"I'm at {current_point}, next is {next_point}, already been to {already_visited}")
    if current_point == 'end':
        # print(f"Got into end.")
        new_visited.append(current_point)
        found_paths.add(tuple(new_visited))
        return new_visited
    if is_small_cave(current_point) and current_point in new_visited:
        # did we get into some cave we've already been in? If so, let's check if we have our chance
        # print(f"Got into small cave case.")
        if not special_chance:
            return new_visited
        special_chance = False
    if current_point == 'start' and len(already_visited) > 0:
        return new_visited
    new_visited.append(current_point)
    return [traverse_cave(a, b, new_visited, special_chance) for a, b in tuples if a == next_point]


# change last argument to False for basic case
[traverse_cave(a, b, [], True) for a, b in tuples if a == 'start']
print(found_paths)
print(f"Found paths length: {len(found_paths)}")