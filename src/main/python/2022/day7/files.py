day_7_input_path = '../../../resources/2022/day7-input'


values_f = open(day_7_input_path, 'r')
lines = values_f.readlines()

dirs = {'/': [0, {}, None]}
            # w, children, parent

for i in range(len(lines)):
    line = lines[i].strip()
    if line.startswith("$ cd"):
        prompt, _, dirname = line.split(' ')
        if dirname == '/':
            current = dirs['/']
        elif dirname == '..':
            _,_,parent = current
            current = parent
        else:
            _, children, _ = current
            current = children[dirname]
        print(f"pwd {current}")
    elif line.startswith("$ ls"):
        i += 1
        while not i == len(lines) and not lines[i].startswith("$"):
            line = lines[i].strip()
            weight, name = line.split(' ')
            print(f"LSe {weight}, {name}")
            _, children, _ = current
            if weight == 'dir':
                if name not in children:
                    children[name] = [0, {}, current]
            else:
                if name not in children:
                    children[name] = [int(weight), None, current]
            i += 1
        i -= 1

print(f"{dirs}")


def weight_dirs(dir):
    weight, children, _ = dir
    if children is None or len(children) == 0 or weight != 0:
        return weight
    for child in children.values():
        weight += weight_dirs(child)
    dir[0] = weight
    return weight


currently_taken = weight_dirs(dirs['/'])
print(f" Full weight is: {currently_taken}")
ALL_SIZE = 70000000
MINIMUM_REQUIRED = 30000000
left_size = ALL_SIZE - currently_taken
required_more = MINIMUM_REQUIRED - left_size
print(f"There is {left_size} left, we need {required_more} more")

print(f"{dirs}")

sizes = []

def find_all_below(dir, threshold):
    weight, children, parent = dir
    sum = 0
    if children is not None:
        for child in children.values():
            sum += find_all_below(child, threshold)
        if weight > threshold:
            print(f"Current dir weight {weight}")
            sizes.append(weight)
            return sum + weight
    return sum


print(f"{find_all_below(dirs['/'], required_more)}")
sizes.sort()
print(f"{sizes}")