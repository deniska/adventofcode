import sys

world = {}
dirs = [(1, 0), (0, 1), (-1, 0), (0, -1)]

with open(sys.argv[1]) as f:
    for y, line in enumerate(f):
        for x, c in enumerate(line.strip()):
            world[x, y] = c

width = x + 1
height = y + 1

def flood_fill(x, y):
    letter = world[x, y]
    visited = {(x, y)}
    frontier = {(x, y)}
    perimeter = 0
    while frontier:
        x, y = frontier.pop()
        for dx, dy in dirs:
            nx = x + dx
            ny = y + dy
            if (nx, ny) in visited:
                continue
            if world.get((nx, ny)) != letter:
                perimeter += 1
                continue
            visited.add((nx, ny))
            frontier.add((nx, ny))
    return visited, perimeter

def calc_sides(area):
    letter = world[next(iter(area))]
    cnt = 0
    # north
    for y in range(height):
        side = False
        for x in range(width + 1):
            if (x, y) in area and world.get((x, y)) == letter and world.get((x, y - 1)) != letter:
                side = True
            else:
                if side:
                    cnt += 1
                side = False
    # south
    for y in range(height):
        side = False
        for x in range(width + 1):
            if (x, y) in area and world.get((x, y)) == letter and world.get((x, y + 1)) != letter:
                side = True
            else:
                if side:
                    cnt += 1
                side = False
    # west
    for x in range(width):
        side = False
        for y in range(height + 1):
            if (x, y) in area and world.get((x, y)) == letter and world.get((x - 1, y)) != letter:
                side = True
            else:
                if side:
                    cnt += 1
                side = False
    # east
    for x in range(width):
        side = False
        for y in range(height + 1):
            if (x, y) in area and world.get((x, y)) == letter and world.get((x + 1, y)) != letter:
                side = True
            else:
                if side:
                    cnt += 1
                side = False
    return cnt

def go():
    s = 0
    s2 = 0
    w = world.copy()
    while w:
        visited, perimeter = flood_fill(*next(iter(w.keys())))
        s += len(visited) * perimeter
        s2 += len(visited) * calc_sides(visited)
        for v in visited:
            del w[v]
    print(s)
    print(s2)

go()
