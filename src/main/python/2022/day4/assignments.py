day_4_input_path = '../../../resources/2022/day4-input'


values_f = open(day_4_input_path, 'r')
values_groups = [x.strip().split(",") for x in values_f.readlines()]
values = [([int(x) for x in x[0].split("-")], [int(x) for x in x[1].split("-")]) for x in values_groups]

print(f"{values}")


def first(values):
    overlaps = 0
    for one, sec in values:
        if sec[0] >= one[0] and sec[1] <= one[1]:
            overlaps += 1
        elif one[0] >= sec[0] and one[1] <= sec[1]:
            overlaps += 1

    print(f"First overlaps count: {overlaps}")


def second(values):
    overlaps = 0
    for one, sec in values:
        if sec[0] <= one[1] <= sec[1] or one[0] <= sec[1] <= one[1]:
            overlaps += 1

    print(f"Second overlaps: {overlaps}")


first(values)
second(values)