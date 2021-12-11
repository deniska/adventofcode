import sys
import itertools

cubes = set()
with open(sys.argv[1]) as f:
    for x, line in enumerate(f):
        for y, c in enumerate(line.strip()):
            if c == '#':
                cubes.add((x, y, 0))

def iter_neighbours(x, y, z):
    for i, j, k in itertools.product(*[range(-1, 2)]*3):
        if (i, j, k) == (0, 0, 0):
            continue
        yield x+i, y+j, z+k

def count_neighbours(cubes, x, y, z):
    s = 0
    for c in iter_neighbours(x, y, z):
        if c in cubes:
            s += 1
    return s

for _ in range(6):
    next_cubes = set()
    for c in cubes:
        if count_neighbours(cubes, *c) in (2, 3):
            next_cubes.add(c)
        for c1 in iter_neighbours(*c):
            if count_neighbours(cubes, *c1) == 3:
                next_cubes.add(c1)
    cubes = next_cubes

print(len(cubes))
