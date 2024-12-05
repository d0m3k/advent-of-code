import math

input_path = '../../../resources/2024/day5'

values_f = open(input_path, 'r')

rules = {}
legal_updates = []


def is_legal(current_update, rules):
    # for each item, get the map and check if any value on the right is after it; if yes, return False; return True at the end
    for i in range(len(current_update)):
        current = current_update[i]
        rules_for_current = rules.get(current, set())
        for j in range(i+1, len(current_update)):
            if current_update[j] in rules_for_current:
                return False
    return True


for line in values_f.readlines():
    if '|' in line:
        # parse rule saving them to map, where RIGHT IS KEY
        left, right = line.strip().split("|")
        rules[right] = rules.get(right, set())
        rules[right].add(left)
    if ',' in line:
        # parse update
        current_update = line.strip().split(",")
        if is_legal(current_update, rules):
            legal_updates.append(current_update)


print(f"Rules: {rules}, \nlegal_updates: {legal_updates}")

result = 0
for update in legal_updates:
    middle_element = update[math.ceil(len(update)/2)-1]
    print(f"Adding middle element {middle_element}")
    result += int(middle_element)

print(f"Result: {result}")
