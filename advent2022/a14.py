import sys

walls = set()
sand = set()

with open(sys.argv[1]) as f:
    for line in f:
        path = line.strip().split(' -> ')
        path = [(int((a := p.split(','))[0]), int(a[1])) for p in path]
        x, y = path[0]
        walls.add(path[0])
        for p in path[1:]:
            x1, y1 = p
            if x1 == x:
                for i in range(y, y1, 1 if y < y1 else -1):
                    walls.add((x, i))
            elif y1 == y:
                for i in range(x, x1, 1 if x < x1 else -1):
                    walls.add((i, y))
            walls.add(p)
            x, y = p

def can_move(x, y, floor):
    if (x, y) not in sand and (x, y) not in walls and y < floor:
        return True
    return False

def part(part_num):
    done = False
    sand.clear()
    if part_num == 1:
        floor = 999999
    else:
        floor = 0
        for x, y in walls:
            floor = max(y+2, floor)
    while not done:
        x = 500
        y = 0
        while True:
            if can_move(x, y + 1, floor):
                y += 1
            elif can_move(x - 1, y + 1, floor):
                x -= 1
                y += 1
            elif can_move(x + 1, y + 1, floor):
                x += 1
                y += 1
            else:
                sand.add((x, y))
                break
            if y > 999:
                done = True
                break
        if (500, 0) in sand:
            break
    print(len(sand))

part(1)
part(2)
