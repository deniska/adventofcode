import sys

dirs = [(0, 1), (1, 0), (-1, 0), (0, -1)]
m = {}
with open(sys.argv[1]) as f:
    for y, line in enumerate(f):
        for x, c in enumerate(line.strip()):
            m[x, y] = int(c)

def find_nines(x, y):
    c = m.get((x, y))
    if c == 9:
        return {(x, y)}
    s = set()
    for dx, dy in dirs:
        if m.get((x + dx, y + dy)) != (c + 1):
            continue
        s |= find_nines(x + dx, y + dy)
    return s

def count_paths(x, y):
    c = m.get((x, y))
    if c == 9:
        return 1
    s = 0
    for dx, dy in dirs:
        if m.get((x + dx, y + dy)) != (c + 1):
            continue
        s += count_paths(x + dx, y + dy)
    return s

s = 0
for (x, y), c in m.items():
    if c == 0:
        s += len(find_nines(x, y))
print(s)

s = 0
for (x, y), c in m.items():
    if c == 0:
        s += count_paths(x, y)
print(s)
