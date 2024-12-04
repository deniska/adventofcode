import sys

with open(sys.argv[1]) as f:
    data = f.read()

x = 0
y = 0
houses = {(0, 0)}

for c in data:
    if c == '>':
        x += 1
    elif c == '<':
        x -= 1
    elif c == 'v':
        y += 1
    elif c == '^':
        y -= 1
    houses.add((x, y))

print(len(houses))

sx = 0
sy = 0
rx = 0
ry = 0
turn = False
houses = {(0, 0)}

for c in data:
    if turn:
        x, y = sx, sy
    else:
        x, y = rx, ry
    if c == '>':
        x += 1
    elif c == '<':
        x -= 1
    elif c == 'v':
        y += 1
    elif c == '^':
        y -= 1
    if turn:
        sx, sy = x, y
    else:
        rx, ry = x, y
    turn = not turn
    houses.add((x, y))

print(len(houses))
