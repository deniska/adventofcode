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

def score(x, y):
    if x == 0 or y == 0 or x == w-1 or y == h-1:
        return 0

    return score_left(x, y) * score_right(x, y) * score_top(x, y) * score_bottom(x, y)

def score_left(x, y):
    s = 0
    for i in range(x-1, -1, -1):
        s += 1
        if trees[i, y] >= trees[x, y]:
            break
    return s

def score_right(x, y):
    s = 0
    for i in range(x+1, w):
        s += 1
        if trees[i, y] >= trees[x, y]:
            break
    return s

def score_top(x, y):
    s = 0
    for j in range(y-1, -1, -1):
        s += 1
        if trees[x, j] >= trees[x, y]:
            break
    return s

def score_bottom(x, y):
    s = 0
    for j in range(y+1, h):
        s += 1
        if trees[x, j] >= trees[x, y]:
            break
    return s

p2 = 0

for i in range(w):
    for j in range(h):
        p2 = max(p2, score(i, j))
print(p2)
