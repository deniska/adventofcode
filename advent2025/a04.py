import sys

rolls = set()

with open(sys.argv[1]) as f:
    for y, line in enumerate(f):
        for x, c in enumerate(line.strip()):
            if c == '@':
                rolls.add((x, y))

p1 = 0
p2 = 0

first = True

while True:
    to_remove = set()
    for (x, y) in rolls:
        c = 0
        for dx in range(-1, 2):
            for dy in range(-1, 2):
                if dx == 0 and dy == 0: continue
                if (x + dx, y + dy) in rolls:
                    c += 1
        if c < 4:
            if first:
                p1 += 1
            p2 += 1
            to_remove.add((x, y))
    if not to_remove:
        break
    rolls = rolls - to_remove
    first = False

print(p1)
print(p2)
