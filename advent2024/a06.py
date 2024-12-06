import sys

walls = set()

with open(sys.argv[1]) as f:
    for y, line in enumerate(f):
        line = line.strip()
        for x, c in enumerate(line):
            if c == '#':
                walls.add((x, y))
            elif c == '^':
                start_x = x
                start_y = y

width = x + 1
height = y + 1

dirs = [(0, -1), (1, 0), (0, 1), (-1, 0)]

def part1(width, height, walls, start_x, start_y):
    x = start_x
    y = start_y
    visited = {(x, y)}
    d = 0
    while True:
        dx, dy = dirs[d]
        nx = x + dx
        ny = y + dy
        if (nx, ny) in walls:
            d += 1
            d %= len(dirs)
            continue
        elif nx < 0 or ny < 0 or nx >= width or ny >= height:
            break
        x = nx
        y = ny
        visited.add((x, y))
    print(len(visited))

def is_loopy(width, height, walls, start_x, start_y):
    x = start_x
    y = start_y
    d = 0
    visited_rotations = set()
    while True:
        dx, dy = dirs[d]
        nx = x + dx
        ny = y + dy
        if (nx, ny) in walls:
            d += 1
            d %= len(dirs)
            if (nx, ny, d) in visited_rotations:
                return True
            visited_rotations.add((nx, ny, d))
            continue
        elif nx < 0 or ny < 0 or nx >= width or ny >= height:
            return False
        x = nx
        y = ny

def part2(width, height, walls, start_x, start_y):
    cnt = 0
    for x in range(width):
        for y in range(height):
            if (x, y) in walls:
                continue
            if is_loopy(width, height, walls | {(x, y)}, start_x, start_y):
                cnt += 1
    print(cnt)

part1(width, height, walls, start_x, start_y)
part2(width, height, walls, start_x, start_y)
