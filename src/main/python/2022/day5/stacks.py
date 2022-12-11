import re

day_5_input_path = '../../../resources/2022/day5-input'


values_f = open(day_5_input_path, 'r')
lines = [x for x in values_f.readlines()]


stacks = {}
result_stacks = {}

def parse_stacks_line(line, stacks):
    print(f"Parsing {line}")
    next_letters = []
    for i in range(len(line)):
        if i % 4 == 1:
            next_letters.append(line[i].strip())
    # next_letters = [re.search('(\\w)', l).group(0) for l in line.split(' ')]
    print(next_letters)
    for i in range(1, len(next_letters)+1):
        if next_letters[i-1] == '':
            pass
        else:
            if i not in stacks:
                stacks[i] = []
            stacks[i].insert(0, next_letters[i-1])
    print(f"after insterting: {stacks}")


def move(line, stacks):
    s = re.search('(\\d+) from (\\d+) to (\\d+)', line)
    count, froms, tos = int(s.group(1)), int(s.group(2)), int(s.group(3))
    print(f"Before {count, froms, tos}: {stacks}")
    #first iteration:
    #for i in range(count):
    #    value = stacks[froms].pop()
    #    stacks[tos].append(value)

    # second interation
    values = stacks[froms][-count:]
    stacks[tos].extend(values)
    for i in range(count):
        stacks[froms].pop()
    print(f"After  {count, froms, tos}: {stacks}")



for line in lines:
    if line != '' and not line.strip().startswith("1") and not line.startswith("move"):
        parse_stacks_line(line, stacks)
    elif line.startswith("move"):
        move(line, stacks)

print(f"Stacks: {stacks}")
for i in range(1, len(stacks.keys())+1):
    print(f"{stacks[i].pop()}")