import sys

w = {}
moves = []
with open(sys.argv[1]) as f:
    for y, line in enumerate(f):
        line = line.strip()
        if line == '':
            break
        for x, c in enumerate(line):
            if c == '@':
                start_x = x
                start_y = y
            elif c != '.':
                w[x, y] = c
    for line in f:
        moves.extend(line.strip())

dirs = {
    'v': (0, 1),
    '>': (1, 0),
    '<': (-1, 0),
    '^': (0, -1),
}

x = start_x
y = start_y
for move in moves:
    dx, dy = dirs[move]
    nx = x
    ny = y
    moved_box = False
    can_move = True
    while True:
        nx = nx + dx
        ny = ny + dy
        c = w.get((nx, ny))
        if c == 'O':
            moved_box = True
        elif c == '#':
            can_move = False
            break
        else:
            break
    if can_move:
        if moved_box:
            w[nx, ny] = 'O'
            del w[x + dx, y + dy]
        x = x + dx
        y = y + dy

s = 0
for (x, y), c in w.items():
    if c == 'O':
        s += y * 100 + x
print(s)

w = {}
moves = []
with open(sys.argv[1]) as f:
    for y, line in enumerate(f):
        line = line.strip()
        if line == '':
            break
        for x, c in enumerate(line):
            if c == '@':
                start_x = x * 2
                start_y = y
            elif c == '#':
                w[x*2, y] = '#'
                w[x*2 + 1, y] = '#'
            elif c == 'O':
                w[x*2, y] = '['
                w[x*2 + 1, y] = ']'
    for line in f:
        moves.extend(line.strip())

def print_world():
    width = max(a[0] for a in w) + 1
    height = max(a[1] for a in w) + 1
    for py in range(height):
        for px in range(width):
            c = w.get((px, py))
            if px == x and py == y:
                print('@', end='')
            elif c in ('[', ']', '#'):
                print(c, end='')
            else:
                print('.', end='')
        print()


x = start_x
y = start_y
#print_world()
for move in moves:
    #print(move)
    dx, dy = dirs[move]
    can_move = True
    moved_boxes = set()
    if dx != 0:
        nx = x
        ny = y
        while True:
            nx += dx
            c = w.get((nx, ny))
            if c in ('[', ']'):
                moved_boxes.add((nx, ny))
            elif c == '#':
                can_move = False
                break
            else:
                break
    else:
        nx = x
        ny = y
        moving_frontier = {x}
        can_move = True
        while moving_frontier:
            next_moving_frontier = set()
            ny += dy
            for fx in moving_frontier:
                c = w.get((fx, ny))
                if c == '[':
                    next_moving_frontier.add(fx)
                    next_moving_frontier.add(fx + 1)
                    moved_boxes.add((fx, ny))
                    moved_boxes.add((fx + 1, ny))
                elif c == ']':
                    next_moving_frontier.add(fx)
                    next_moving_frontier.add(fx - 1)
                    moved_boxes.add((fx, ny))
                    moved_boxes.add((fx - 1, ny))
                elif c == '#':
                    can_move = False
                    next_moving_frontier = set()
                    break
            moving_frontier = next_moving_frontier
    if can_move:
        x += dx
        y += dy
        next_w = w.copy()
        for box in moved_boxes:
            del next_w[box]
        for bx, by in moved_boxes:
            next_w[bx + dx, by + dy] = w[bx, by]
        w = next_w
    #print_world()

s = 0
for (x, y), c in w.items():
    if c == '[':
        s += y * 100 + x
print(s)
