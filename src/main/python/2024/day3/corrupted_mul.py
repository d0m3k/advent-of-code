import re

input_path = '../../../resources/2024/day3'

values_f = open(input_path, 'r')

pattern = r"(mul\((\d{1,3}),(\d{1,3})\))"

to_parse = ""

for line in values_f.readlines():
    to_parse += line

matches = re.compile(pattern).findall(to_parse)

print(f"Matches: {matches}")

result = 0

for match in matches:
    full, a_str, b_str = match
    a, b = int(a_str), int(b_str)
    result += a*b

print(f"Result: {result}")
