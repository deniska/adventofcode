import re
import sys

with open(sys.argv[1]) as f:
    data = f.read()

s = 0
for m in re.findall(r'mul\((\d+),(\d+)\)', data):
    s += int(m[0]) * int(m[1])

print(s)

s = 0
enabled = True
for m in re.findall(r"(mul)\((\d+),(\d+)\)|(do)\(\)|(don't)\(\)", data):
    if m[0] == 'mul' and enabled:
        s += int(m[1]) * int(m[2])
    elif m[3] == 'do':
        enabled = True
    elif m[4] == "don't":
        enabled = False
print(s)
