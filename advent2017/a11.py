def cubehexdist(x, y, z):
    return (abs(x) + abs(y) + abs(z)) // 2

def hexdist(s):
    dirs = s.strip().split(',')
    x = 0
    y = 0
    z = 0
    m = 0
    for d in dirs:
        dx, dy, dz = {
                'n': (1, 0, -1),
                'ne': (1, -1, 0),
                'se': (0, -1, 1),
                's': (-1, 0, 1),
                'sw': (-1, 1, 0),
                'nw': (0, 1, -1),
                }[d]
        x += dx
        y += dy
        z += dz
        m = max(cubehexdist(x, y, z), m)
    return cubehexdist(x, y, z), m

with open('input11.txt') as f:
    print(hexdist(f.read()))
