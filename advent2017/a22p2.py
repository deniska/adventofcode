import numpy as np

grid = np.zeros((10000, 10000), np.int32)

with open('input22.txt') as f:
    for i, line in enumerate(f):
        for j, c in enumerate(line):
            if c == '#':
                grid[5000+j, 5000+i] = 2

x = 5000 + j//2
y = 5000 + i//2

d = 1 # 0 - r, 1 - u, 2 - l, 3 - d
dxs = [1, 0, -1, 0]
dys = [0, -1, 0, 1]

z = 0

for i in range(10_000_000):
    v = grid[x, y]
    if v == 0:
        d += 1
    elif v == 1:
        z += 1
    elif v == 2:
        d -= 1
    elif v == 3:
        d += 2
    grid[x, y] += 1
    grid[x, y] %= 4
    d %= 4
    x += dxs[d]
    y += dys[d]

print(z)
