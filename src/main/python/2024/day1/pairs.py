input_path = '../../../resources/2024/day1e'

values_f = open(input_path, 'r')

left_col, right_col = [], []

for line in values_f.readlines():
    left, right =  line.strip().split()
    left_col.append(int(left))
    right_col.append(int(right))

left_col.sort()
right_col.sort()

result = 0

for i in range(len(left_col)):
    result = result + abs(left_col[i]-right_col[i])

print(f"Result: {result}")