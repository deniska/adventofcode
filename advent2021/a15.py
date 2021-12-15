import sys

grid = {}

with open(sys.argv[1]) as f:
    for y, line in enumerate(f):
        for x, c in enumerate(line.strip()):
            grid[x, y] = int(c)

w = x + 1
h = y + 1

neighbours = [
        (-1, 0),
        (0, -1),
        (0, 1),
        (1, 0),
        ]

def part1(grid=grid, w=w, h=h):
    distances = {(0, 0): 0}
    seen = set()
    frontier = {(0, 0)}
    while frontier:
        pt = min(frontier, key=lambda x: distances[x])
        frontier.remove(pt)
        dist = distances[pt]
        for dx, dy in neighbours:
            nx = pt[0] + dx
            ny = pt[1] + dy
            if (nx, ny) in seen:
                continue
            if (nx, ny) not in grid:
                continue
            frontier.add((nx, ny))
            a = grid[nx, ny]
            distances[nx, ny] = min(dist+a, distances.get((nx, ny), 999999))
        seen.add(pt)
    return distances[w-1, h-1]

def part2():
    g = grid.copy()
    for i in range(0, 5):
        for j in range(0, 5):
            for x in range(w):
                for y in range(h):
                    g[x + w*i, y + h*j] = (g[x, y] + i + j - 1) % 9 + 1
    return part1(g, w*5, h*5)

print(part1())
print(part2())
