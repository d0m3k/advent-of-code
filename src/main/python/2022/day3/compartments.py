day_2_input_path = '../../../resources/2022/day3-input'


values_f = open(day_2_input_path, 'r')
values_groups = [x.strip() for x in values_f.readlines()]
values = [(x[:len(x) // 2], x[len(x) // 2:]) for x in values_groups]

print(f"{values}, {values_groups}")

def value_of(char):
    val = ord(char)
    if 97 <= val <= 122:
        return val - 96
    if 65 <= val <= 90:
        return val - 38


def intersect(set1, set2):
    result = set()
    for a in set1:
        if a in set2:
            result.add(a)
    return result


def result1(values):
    result = 0
    for left, right in values:
        sleft, sright = set(left), set(right)
        dupe = intersect(sleft, sright).pop()
        print(f"Dupe is {dupe}, will add {value_of(dupe)}")
        result += value_of(dupe)
    print(f"Result 1 is {result}")


def result2(values):
    result_value = 0
    print(f"Range is {range(1, len(values) // 3 + 1)}")
    for i in range(0, len(values) // 3):
        off = 3*i
        v1, v2, v3 = values[off], values[off+1], values[off+2]
        results = intersect(v1, v2)
        results = intersect(results, v3)
        result = results.pop()
        val = value_of(result)
        print(f"We got {(v1, v2, v3)}, result is {result}, value {val}")
        result_value += val
    print(f"Result 2 is {result_value}")


result1(values)
result2(values_groups)
