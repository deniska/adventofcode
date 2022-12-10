import sys

trees = {}
w = 0
h = 0

with open(sys.argv[1]) as f:
    for i, line in enumerate(f):
        line = line.strip()
        h += 1
        w = len(line)
        for j, c in enumerate(line):
            trees[j, i] = int(c)

def is_seen(x, y):
    if x == 0 or y == 0 or x == w-1 or y == h-1:
        return True

    if seen_left(x, y) or seen_right(x, y) or seen_top(x, y) or seen_bottom(x, y):
        return True

    return False

def seen_left(x, y):
    for i in range(x-1, -1, -1):
        if trees[i, y] >= trees[x, y]:
            return False
    return True

def seen_right(x, y):
    for i in range(x+1, w):
        if trees[i, y] >= trees[x, y]:
            return False
    return True

def seen_top(x, y):
    for j in range(y-1, -1, -1):
        if trees[x, j] >= trees[x, y]:
            return False
    return True

def seen_bottom(x, y):
    for j in range(y+1, h):
        if trees[x, j] >= trees[x, y]:
            return False
    return True

p1 = 0

for i in range(w):
    for j in range(h):
        if is_seen(i, j):
            p1 +=1
print(p1)
