import sys
import re

with open(sys.argv[1]) as f:
    data = f.readlines()

data = list(map(list, zip(*data)))

p2 = 0

for line in data:
    line = ''.join(line).strip()
    if '+' in line:
        op = '+'
        res = 0
    elif '*' in line:
        op = '*'
        res = 1
    elif not line:
        p2 += res
        continue
    num = int(re.search(r'\d+', line)[0])
    if op == '+':
        res += num
    else:
        res *= num

print(p2)
