import sys
import itertools

tiles = []
xs = set()
ys = set()

with open(sys.argv[1]) as f:
    for line in f:
        x, y = line.strip().split(',')
        x = int(x)
        y = int(y)
        tiles.append((x, y))
        xs.add(x)
        ys.add(y)

xs = sorted(xs)
ys = sorted(ys)

segs = []
for a, b in itertools.pairwise(tiles):
    segs.append((*a, *b))
segs.append((*tiles[-1], *tiles[0]))

vert_segs = [s for s in segs if s[0] == s[2]]
vert_segs.sort()

def scan_line(y):
    ranges = []
    inside = False
    for x1, y1, x2, y2 in vert_segs:
        if y1 <= y <= y2 or y2 <= y <= y1:
            if not inside:
                inside = True
                w = y1 < y2
                x = x1
            else:
                if (y1 < y2) != w:
                    inside = False
                    ranges.append(range(x, x1+1))
    return ranges

ranges = {}
for y in ys:
    ranges[y] = scan_line(y)

def fits(x1, y1, x2, y2):
    x1, x2 = sorted((x1, x2))
    y1, y2 = sorted((y1, y2))
    for y in ys:
        if not (y1 <= y <= y2): continue
        for x in xs:
            if not (x1 <= x <= x2): continue
            for r in ranges[y]:
                if x in r:
                    break
            else:
                return False
    return True

p1 = 0
p2 = 0
for i in range(len(tiles)-1):
    x1, y1 = tiles[i]
    for j in range(i, len(tiles)):
        x2, y2 = tiles[j]
        if (s := (abs(x1 - x2) + 1) * (abs(y1 - y2) + 1)) > p1:
            p1 = s
        if s > p2 and fits(x1, y1, x2, y2):
            p2 = s
print(p1)
print(p2)
