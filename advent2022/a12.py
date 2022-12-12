import sys

heightmap = {}
neighbours = [
    (1, 0),
    (0, 1),
    (-1, 0),
    (0, -1),
]

with open(sys.argv[1]) as f:
    y = 0
    for line in f:
        line = line.strip()
        for x, c in enumerate(line):
            if c == 'S':
                c = 'a'
                start = (x, y)
            elif c == 'E':
                c = 'z'
                end = (x, y)
            heightmap[x, y] = ord(c) - ord('a')
        y += 1

def part1(start=start):
    distances = {start: 0}
    seen = set()
    frontier = {start}
    while frontier:
        pt = min(frontier, key=lambda x: distances[x])
        frontier.remove(pt)
        dist = distances[pt]
        for dx, dy in neighbours:
            nx = pt[0] + dx
            ny = pt[1] + dy
            if (nx, ny) in seen:
                continue
            if (nx, ny) not in heightmap:
                continue
            if heightmap[nx, ny] - heightmap[pt] > 1:
                continue
            frontier.add((nx, ny))
            distances[nx, ny] = min(dist+1, distances.get((nx, ny), 999999))
        seen.add(pt)
    return distances.get(end)

print(part1())

def part2():
    lengths = []
    for k, v in heightmap.items():
        if v == 0:
            l = part1(start=k)
            if l is None:
                continue
            lengths.append(l)
    return min(lengths)

print(part2())
