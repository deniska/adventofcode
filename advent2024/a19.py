import sys
import functools

designs = []
with open(sys.argv[1]) as f:
    towels = f.readline().strip().split(', ')
    f.readline()
    for line in f:
        designs.append(line.strip())

@functools.cache
def count_ways(design, start_idx=0):
    if start_idx == len(design):
        return 1
    c = 0
    for t in towels:
        if design.startswith(t, start_idx):
            c += count_ways(design, start_idx + len(t))
    return c

c = 0
s = 0
for d in designs:
    w = count_ways(d)
    s += w
    if w > 0:
        c += 1
print(c)
print(s)
