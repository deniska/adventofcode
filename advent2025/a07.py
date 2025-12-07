import sys
import functools

splitters = set()

with open(sys.argv[1]) as f:
    for y, line in enumerate(f):
        for x, c in enumerate(line):
            if c == 'S':
                start_x = x
            elif c == '^':
                splitters.add((x, y))
height = y + 1

p1 = 0

tachyons = {start_x}
for y in range(1, height):
    next_tachyons = set()
    for tachyon in tachyons:
        if (tachyon, y) in splitters:
            next_tachyons.add(tachyon-1)
            next_tachyons.add(tachyon+1)
            p1 += 1
        else:
            next_tachyons.add(tachyon)
    tachyons = next_tachyons

print(p1)

@functools.cache
def quantum(x, y):
    if y >= height:
        return 1
    elif (x, y) in splitters:
        return quantum(x-1, y+1) + quantum(x+1, y+1)
    else:
        return quantum(x, y+1)

p2 = quantum(start_x, 0)
print(p2)
