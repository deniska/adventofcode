import sys

def main():
    with open(sys.argv[1]) as f:
        wire1s = f.readline().strip()
        wire2s = f.readline().strip()

    wire1, w1d = wire(wire1s)
    wire2, w2d = wire(wire2s)
    intersections = wire1 & wire2
    shortest = min(dist(i) for i in intersections)
    print(shortest)
    shortest2 = min(w1d[i] + w2d[i] for i in intersections)
    print(shortest2)

dirs = {
        'U': (0, 1),
        'D': (0, -1),
        'L': (-1, 0),
        'R': (1, 0),
        }

def wire(s):
    x = 0
    y = 0
    d = 0
    segments = set()
    dists = {}
    for segment in s.split(','):
        dx, dy = dirs[segment[0]]
        for _ in range(int(segment[1:])):
            x += dx
            y += dy
            d += 1
            segments.add((x, y))
            if not (x, y) in dists:
                dists[x, y] = d
    return segments, dists

def dist(i):
    return abs(i[0]) + abs(i[1])

if __name__ == '__main__':
    main()
