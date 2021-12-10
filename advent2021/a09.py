import sys

m = {}

h = 0
with open(sys.argv[1]) as f:
    for line in f:
        line = line.strip()
        w = len(line)
        for i, c in enumerate(line):
            m[i, h] = int(c)
        h += 1

def basin(x, y):
    b = 0
    to_check = {(x, y)}
    seen = set()
    while to_check:
        next_check = set()
        for i, j in to_check:
            if get(i, j) == 9:
                continue
            seen.add((i, j))
            b += 1
            for nx, ny in neighbours(i, j):
                if (nx, ny) not in seen:
                    next_check.add((nx, ny))
        to_check = next_check
    return b

def neighbours(x, y):
    yield x + 1, y
    yield x - 1, y
    yield x, y - 1
    yield x, y + 1

def get(x, y):
    return m.get((x, y), 9)

c = 0
basins = []
for i in range(w):
    for j in range(h):
        a = m[i, j]
        if (a < get(i - 1, j)
                and a < get(i + 1, j)
                and a < get(i, j - 1)
                and a < get(i, j + 1)):
            c += 1 + a
            basins.append(basin(i, j))
print(c)
basins.sort(reverse=True)
print(basins[0] * basins[1] * basins[2])
