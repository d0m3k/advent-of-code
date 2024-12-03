import re

input_path = '../../../resources/2024/day3'

values_f = open(input_path, 'r')

pattern = r"(mul\((\d{1,3}),(\d{1,3})\))"
pattern_omit = r"(don't\(\).*?do\(\))"


to_parse = ""

for line in values_f.readlines():
    to_parse += line


def clean_donts(input_string):
    result = input_string
    while "don't()" in result:
        dont_pos = result.find("don't()")
        if dont_pos == -1:
            break

        do_pos = result.find("do()", dont_pos)

        if do_pos != -1:
            result = result[:dont_pos] + result[do_pos + len("do()"):]
        else:
            result = result[:dont_pos]

    return result

to_parse = clean_donts(to_parse)

matches = re.compile(pattern).findall(to_parse)

print(f"Matches: {matches}")

result = 0

for match in matches:
    full, a_str, b_str = match
    a, b = int(a_str), int(b_str)
    result += a*b

print(f"Result: {result}")
