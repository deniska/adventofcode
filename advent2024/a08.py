import sys
import math
import collections

antenna_letters = collections.defaultdict(list)
with open(sys.argv[1]) as f:
    for y, line in enumerate(f):
        for x, c in enumerate(line.strip()):
            if c == '.':
                continue
            antenna_letters[c].append((x, y))

width = x + 1
height = y + 1

nodes = set()
for antennas in antenna_letters.values():
    for antenna1 in antennas:
        for antenna2 in antennas:
            if antenna1 == antenna2:
                continue
            x = 2*antenna2[0] - antenna1[0]
            y = 2*antenna2[1] - antenna1[1]
            if x >= 0 and x < width and y >= 0 and y < height:
                nodes.add((x, y))

print(len(nodes))

nodes = set()
for antennas in antenna_letters.values():
    for antenna1 in antennas:
        for antenna2 in antennas:
            if antenna1 == antenna2:
                continue
            dx = antenna2[0] - antenna1[0]
            dy = antenna2[1] - antenna1[1]
            assert(math.gcd(abs(dx), abs(dy)) == 1)
            x = antenna2[0]
            y = antenna2[1]
            while x >= 0 and x < width and y >= 0 and y < height:
                nodes.add((x, y))
                x += dx
                y += dy
print(len(nodes))
