import sys
import json

with open(sys.argv[1]) as f:
    j = json.load(f)

def count(j, part2=False):
    s = 0
    if isinstance(j, dict):
        for key, value in j.items():
            if part2 and value == 'red':
                return 0
            s += count(value, part2)
    elif isinstance(j, list):
        for value in j:
            s += count(value, part2)
    elif isinstance(j, int):
        return j
    return s

p1 = count(j)
p2 = count(j, True)
print(p1)
print(p2)
