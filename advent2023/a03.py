import sys
import re

part_coords = set()
numbers = []
possible_gears = {}

with open(sys.argv[1]) as f:
    for line_idx, line in enumerate(f):
        for m in re.finditer(r'\d+|[^.]', line.strip()):
            t = m[0]
            if t.isdigit():
                numbers.append((int(t), line_idx, m.start()))
            else:
                part_coords.add((line_idx, m.start()))
                if t == '*':
                    possible_gears[line_idx, m.start()] = set()

s = 0
for number_def in numbers:
    number, number_line_idx, number_char_idx = number_def
    is_part = False
    for line_idx in range(number_line_idx - 1, number_line_idx + 2):
        for char_idx in range(number_char_idx - 1, number_char_idx + len(str(number)) + 1):
            if (line_idx, char_idx) in part_coords:
                is_part = True
                if (line_idx, char_idx) in possible_gears:
                    possible_gears[line_idx, char_idx].add(number_def)
    if is_part:
        s += number
print(s)

s = 0
for possible_gear_nums in possible_gears.values():
    if len(possible_gear_nums) != 2:
        continue
    num1, num2 = possible_gear_nums
    s += num1[0] * num2[0]
print(s)
