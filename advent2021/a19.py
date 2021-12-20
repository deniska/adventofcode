import sys

scanners = []

with open(sys.argv[1]) as f:
    for line in f:
        line = line.strip()
        if not line:
            continue
        if 'scanner' in line:
            scanner = set()
            scanners.append(scanner)
            continue
        x, y, z = map(int, line.split(','))
        scanner.add((x, y, z))

def offset(p0, p1):
    x0, y0, z0 = p0
    x1, y1, z1 = p1
    return x1 - x0, y1 - y0, z1 - z0

def iter_offsets(scanner):
    for point in scanner:
        yield point, offset_scanner(point, scanner)

def offset_scanner(point, scanner):
    return {offset(point, p) for p in scanner}

def neg(p):
    return -p[0], -p[1], -p[2]

def rotate(rotation, p):
    x, y, z = p
    return [ # thanks asdf
            (+x,+y,+z),
            (+x,+z,-y),
            (+x,-y,-z),
            (+x,-z,+y),

            (-x,+y,-z),
            (-x,-z,-y),
            (-x,+z,+y),
            (-x,-y,+z),

            (+y,+z,+x),
            (+y,-z,-x),
            (+y,+x,-z),
            (+y,-x,+z),

            (-y,+z,-x),
            (-y,+x,+z),
            (-y,-x,-z),
            (-y,-z,+x),

            (+z,+x,+y),
            (+z,+y,-x),
            (+z,-x,-y),
            (+z,-y,+x),

            (-z,+x,-y),
            (-z,+y,+x),
            (-z,-x,+y),
            (-z,-y,-x),
            ][rotation]

def iter_rotations(scanner):
    for rot in range(24):
        yield rot, {rotate(rot, pt) for pt in scanner}

def it(scanners_relative_to_0, checked, offsets):
    for idx, scanner0 in scanners_relative_to_0.copy().items():
        for i, scanner in enumerate(scanners):
            if (idx, i) in checked:
                continue
            if i in scanners_relative_to_0:
                continue
            for rotation, rotated_scanner in iter_rotations(scanner):
                for offset0, offset_scanner0 in iter_offsets(scanner0):
                    for offset, scanner_with_offset in iter_offsets(rotated_scanner):
                        if len(offset_scanner0 & scanner_with_offset) >= 12:
                            scanners_relative_to_0[i] = offset_scanner(neg(offset0), scanner_with_offset)
                            print('Found', i)
                            checked.add((idx, i))
                            offsets[i] = (offset[0] - offset0[0],
                                    offset[1] - offset0[1],
                                    offset[2] - offset0[2])
                            return i
            checked.add((idx, i))

def go():
    scanners_relative_to_0 = {0: scanners[0]}
    checked = set()
    offsets = {0: (0, 0, 0)}
    while(len(scanners_relative_to_0) < len(scanners)):
        it(scanners_relative_to_0, checked, offsets)
    pts = set()
    for scanner in scanners_relative_to_0.values():
        pts |= scanner
    print(len(pts))
    d = 0
    for p1 in offsets.values():
        for p2 in offsets.values():
            d = max(d, dist(p1, p2))
    print(d)

def dist(p1, p2):
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1]) + abs(p1[2] - p2[2])

go()
