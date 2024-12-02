input_path = '../../../resources/2024/day1e'

values_f = open(input_path, 'r')

left_col, right_col = [], []

for line in values_f.readlines():
    left, right =  line.strip().split()
    left_col.append(int(left))
    right_col.append(int(right))

count_map = {}

for val in right_col:
    count_map[val] = count_map.get(val, 0) + 1

result = 0

for i in range(len(left_col)):
    result = result + left_col[i] * count_map.get(left_col[i], 0)

print(f"Result: {result}")