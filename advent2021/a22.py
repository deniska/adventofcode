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
        state = False
        for s, (x1, x2, y1, y2, z1, z2) in instructions:
            if x1 <= x <= x2 and y1 <= y <= y2 and z1 <= z <= z2:
                state = s
        c += state
    return c

print(part1())

def part2():
    cubes = []
    for s, c in instructions:
        next_cubes = []
        new_cube = Cube(*c)
        for cube in cubes:
            next_cubes.extend(cube.subtract(new_cube))
        if s:
            next_cubes.append(new_cube)
        cubes = next_cubes
    return sum(c.vol() for c in cubes)

class Cube:

    def __init__(self, x1, x2, y1, y2, z1, z2):
        self.x1 = x1
        self.x2 = x2
        self.y1 = y1
        self.y2 = y2
        self.z1 = z1
        self.z2 = z2
        self.valid = (x1 < x2) and (y1 < y2) and (z1 < z2)

    def __repr__(self):
        x1 = self.x1
        x2 = self.x2
        y1 = self.y1
        y2 = self.y2
        z1 = self.z1
        z2 = self.z2
        return f'Cube({x1}, {x2}, {y1}, {y2}, {z1}, {z2})'

    def subtract(self, a):
        return []

    def vol(self):
        return (self.x2 - self.x1 + 1) * (self.y2 - self.y1 + 1) * (self.z2 - self.z1 + 1)

print(part2())
