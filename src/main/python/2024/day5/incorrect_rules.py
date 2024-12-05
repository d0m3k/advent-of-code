import math

input_path = '../../../resources/2024/day5'

values_f = open(input_path, 'r')

rules = {}
illegal_updates = []


def is_legal(current_update, rules):
    # for each item, get the map and check if any value on the right is after it; if yes, return False; return True at the end
    for i in range(len(current_update)):
        current = current_update[i]
        rules_for_current = rules.get(current, set())
        for j in range(i+1, len(current_update)):
            if current_update[j] in rules_for_current:
                return False
    return True

def fix_update(update, rules):
    # try simple strategy: if we know that we break rules, swap elements in the update
    current_update = update
    # I am too lazy to write something greedy, so just repeat idea with swap at least update-size times XD
    for i in range(len(current_update)):
        for i in range(len(current_update)):
            current = current_update[i]
            rules_for_current = rules.get(current, set())
            for j in range(i+1, len(current_update)):
                if current_update[j] in rules_for_current:
                    current_update[i], current_update[j] = current_update[j], current_update[i]
    return current_update


for line in values_f.readlines():
    if '|' in line:
        # parse rule saving them to map, where RIGHT IS KEY
        left, right = line.strip().split("|")
        rules[right] = rules.get(right, set())
        rules[right].add(left)
    if ',' in line:
        # parse update
        current_update = line.strip().split(",")
        if not is_legal(current_update, rules):
            illegal_updates.append(current_update)


print(f"Rules: {rules}, \nillegal_updates: {illegal_updates}")

fixed_updates = []

for update in illegal_updates:
    fixed_updates.append(fix_update(update, rules))

print(f"Fixed updates: {fixed_updates}")

result = 0
for update in fixed_updates:
    middle_element = update[math.ceil(len(update)/2)-1]
    print(f"Adding middle element {middle_element}")
    result += int(middle_element)

print(f"Result: {result}")
