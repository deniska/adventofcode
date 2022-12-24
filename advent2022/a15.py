import sys
import re

sensors = []
beacons = set()

with open(sys.argv[1]) as f:
    for line in f:
        sx, sy, bx, by = map(int, re.findall(r'-?\d+', line))
        beacons.add((bx, by))
        r = abs(sx - bx) + abs(sy - by)
        sensors.append((sx, sy, r))

def get_ranges(row):
    ranges = []

    for x, y, r in sensors:
        vdist = abs(y - row)
        if vdist > r:
            continue
        hdist = r - vdist
        ranges.append((x-hdist, x+hdist))
        #print(x, y, r, ranges[-1])

    ranges.sort()
    merged_ranges = []
    px1, px2 = ranges[0]
    for nx1, nx2 in ranges[1:]:
        if nx1 > px2:
            merged_ranges.append((px1, px2))
            px1 = nx1
            px2 = nx2
        else:
            px2 = max(nx2, px2)
    merged_ranges.append((px1, px2))
    return merged_ranges

row = 2000000
merged_ranges = get_ranges(row)
c = 0
for x1, x2 in merged_ranges:
    c += x2 - x1 + 1
for bx, by in beacons:
    if by == row:
        c -= 1
print(c)

def part2(max_row):
    for row in range(0, max_row+1):
        ranges = get_ranges(row)
        if len(ranges) == 2:
            (ax1, ax2), (bx1, bx2) = ranges
            assert bx1 - ax2 == 2
            print(4000000*(ax2+1) + row)

part2(4000000)
