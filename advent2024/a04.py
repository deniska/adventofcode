import sys

d = {}

with open(sys.argv[1]) as f:
    for y, line in enumerate(f):
        line = line.strip()
        for x, c in enumerate(line):
            d[x, y] = c

width = x + 1
height = y + 1
dirs = []
for a in range(-1, 2):
    for b in range(-1, 2):
        if a != 0 or b != 0:
            dirs.append((a, b))

def part1():
    cnt = 0
    for x in range(width):
        for y in range(height):
            for dx, dy in dirs:
                if     (d.get((x + 0*dx, y + 0*dy)) == 'X'
                    and d.get((x + 1*dx, y + 1*dy)) == 'M'
                    and d.get((x + 2*dx, y + 2*dy)) == 'A'
                    and d.get((x + 3*dx, y + 3*dy)) == 'S'):
                    cnt += 1
    print(cnt)

def part2():
    cnt = 0
    for x in range(width):
        for y in range(height):
            for a in ('MS', 'SM'):
                for b in ('MS', 'SM'):
                    if (d.get((x, y)) == 'A'
                            and d.get((x - 1, y - 1)) == a[0] and d.get((x + 1, y + 1)) == a[1]
                            and d.get((x - 1, y + 1)) == b[0] and d.get((x + 1, y - 1)) == b[1]):
                        cnt += 1
    print(cnt)

part1()
part2()
