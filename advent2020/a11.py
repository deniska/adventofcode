import sys
import pathlib
import functools
from itertools import product

lines = pathlib.Path(sys.argv[1]).read_text().strip().split('\n')

seats = {}
for j, line in enumerate(lines):
    for i, c in enumerate(line.strip()):
        seats[i, j] = c

width, height = max(seats.keys())
width += 1
height += 1

directions = []
for i, j in product(range(-1, 2), range(-1, 2)):
    if (i, j) == (0, 0):
        continue
    directions.append((i, j))

def neighbours(seats, x, y):
    s = 0
    for i, j in directions:
        if seats.get((x+i, y+j)) == '#':
            s += 1
    return s

def neightbours2(seats, x, y):
    s = 0
    for i, j in directions:
        d = 1
        while True:
            seat = seats.get((x + i * d, y + j * d))
            if seat is None:
                break
            elif seat == 'L':
                break
            elif seat == '#':
                s += 1
                break
            d += 1
    return s

def algo(seats, neighbours, cnt):
    while True:
        new_seats = {}
        changed = False
        for i, j in product(range(width), range(height)):
            seat = seats[i, j]
            if seat == 'L' and neighbours(seats, i, j) == 0:
                new_seats[i, j] = '#'
                changed = True
            elif seat == '#' and neighbours(seats, i, j) >= cnt:
                new_seats[i, j] = 'L'
                changed = True
            else:
                new_seats[i, j] = seat
        seats = new_seats
        if not changed:
            return sum(s == '#' for s in seats.values())

print(algo(seats, neighbours, 4))
print(algo(seats, neightbours2, 5))
