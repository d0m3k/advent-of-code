from functools import reduce

day_9_input_path = '../../resources/day-9-input'

values_f = open(day_9_input_path, 'r')
values = [[int(y) for y in x.strip()] for x in values_f.readlines()]

print(f"{values}")

low_points = []
low_points_locs = []

def is_low_point(i, j):
    val = values[i][j]
    # print(f"Considering values[{i}][{j}] = {val}")

    left = (i-1 < 0 or val < values[i-1][j])
    up = (j-1 < 0 or val < values[i][j-1])
    right = (i >= len(values) - 1 or val < values[i+1][j])
    down = (j >= len(values[i]) - 1 or val < values[i][j+1])

    return left and up and right and down


already_visited = {}


def smallest_neighbour(i, j):
    val = values[i][j]

    left = values[i-1][j] if i-1 >= 0 else 10
    up = values[i][j-1] if j-1 >= 0 else 10
    right = values[i+1][j] if i+1 < len(values) else 10
    down = values[i][j+1] if j+1 < len(values[i]) else 10

    return min(left, up, right, down)


def get_basin(i, j, basin):
    val = values[i][j]
    print(f"Considering values[{i}][{j}] = {val}")

    if (i, j) in already_visited:
        return basin
    already_visited[(i, j)] = True

    if i-1 >= 0 and values[i-1][j] < 9 and smallest_neighbour(i-1, j) == val:
        basin.append((i-1, j))
        get_basin(i-1, j, basin)
    if j-1 >= 0 and values[i][j-1] < 9 and smallest_neighbour(i, j-1) == val:
        basin.append((i, j-1))
        get_basin(i, j-1, basin)
    if i+1 < len(values) and values[i+1][j] < 9 and smallest_neighbour(i+1, j) == val:
        basin.append((i+1, j))
        get_basin(i+1, j, basin)
    if j+1 < len(values[i]) and values[i][j+1] < 9 and smallest_neighbour(i, j+1) == val:
        basin.append((i, j+1))
        get_basin(i, j+1, basin)

    return basin


for i in range(0, len(values)):
    row = values[i]
    for j in range(0, len(row)):
        if is_low_point(i, j):
            print(f"Appending {values[i][j]}")
            low_points.append(values[i][j])
            low_points_locs.append((i, j))

print(f"Locs: {low_points_locs}")
print(f"Low point count: {len(low_points)}")
risk_levels = [x+1 for x in low_points]
print(f"Risk levels: {risk_levels}, sum: {reduce(int.__add__, risk_levels)}")

print(f"BASINS!")
basins = [set(get_basin(i, j, [(i, j)])) for i, j in low_points_locs]

basins.sort(key=len, reverse=True)

top_3_basins = [basins[x] for x in range(0,3)]

print(f"Basins: {basins}, TOP3: {top_3_basins}, sizes: {[len(x) for x in top_3_basins]}")

print(f"Top 3 mul: {reduce(int.__mul__, [len(x) for x in top_3_basins])}")
# height = len(values)
# length = len(values[0])

funMap = "abcdefghijklmnoprstquvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ<>//><';!@#$%^&*(){}_+|?WERTYUIOPPASDFGHJKLXCVBNMqwertyuiopasdfghjklzxcvbnmmasjdhakcjnaxkcjbaskdjhaskjdhskjadnkjhxkjnckjhdkajhsdkjhqwkjehkjahskdjhkfjahkjhdasdasda"

toColor = values.copy()

for basin_index in range(0, len(basins)):
    for (i,j) in basins[basin_index]:
        toColor[i][j] = funMap[basin_index+1]

print("Colored stuff:")
[print("".join([f"{sign}" for sign in line])) for line in toColor]