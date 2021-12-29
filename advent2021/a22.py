import itertools
import sys
import re

instructions = []

with open(sys.argv[1]) as f:
    for line in f:
        state = line.partition(' ')[0]
        coords = [int(a) for a in re.findall(r'-?\d+', line)]
        instructions.append((state == 'on', coords))

def part1():
    c = 0
    for x, y, z in itertools.product(*[range(-50, 51)]*3):
        c += calc_point(x, y, z)
    return c

def calc_point(x, y, z):
    state = False
    for s, (x1, x2, y1, y2, z1, z2) in instructions:
        if x1 <= x <= x2 and y1 <= y <= y2 and z1 <= z <= z2:
            state = s
    return state

print(part1())

def part2():
    x_splits = set()
    y_splits = set()
    z_splits = set()
    for s, (x1, x2, y1, y2, z1, z2) in instructions:
        x_splits.add(x1)
        x_splits.add(x2+1)
        y_splits.add(y1)
        y_splits.add(y2+1)
        z_splits.add(z1)
        z_splits.add(z2+1)
    x_splits = sorted(x_splits)
    y_splits = sorted(y_splits)
    z_splits = sorted(z_splits)
    vol = 0
    for sx1, sx2 in itertools.pairwise(x_splits):
        for sy1, sy2 in itertools.pairwise(y_splits):
            for sz1, sz2 in itertools.pairwise(z_splits):
                state = calc_point(sx1, sy1, sz1)
                if state:
                    vol += (sx2 - sx1) * (sy2 - sy1) * (sz2 - sz1)
    return vol

print(part2())
