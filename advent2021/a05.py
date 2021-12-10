import sys
import collections

with open(sys.argv[1]) as f:
    data = f.read().strip().split('\n')

lines = []
for a in data:
    pt1, pt2 = a.split(' -> ')
    x1, y1 = pt1.split(',')
    x2, y2 = pt2.split(',')
    x1 = int(x1)
    y1 = int(y1)
    x2 = int(x2)
    y2 = int(y2)
    lines.append(((x1, y1), (x2, y2)))


board = collections.Counter()

for (x1, y1), (x2, y2) in lines:
    if x1 == x2:
        for a in range(min(y1, y2), max(y1, y2) + 1):
            board[x1, a] += 1
    elif y1 == y2:
        for a in range(min(x1, x2), max(x1, x2) + 1):
            board[a, y1] += 1

cnt = 0
for i in board.values():
    if i > 1:
        cnt += 1
print(cnt)

for (x1, y1), (x2, y2) in lines:
    if x1 != x2 and y1 != y2:
        if x1 < x2:
            xs = 1
        else:
            xs = -1
        if y1 < y2:
            ys = 1
        else:
            ys = -1
        for a in range(abs(x1 - x2) + 1):
            board[x1 + xs*a, y1 + ys*a] += 1

cnt = 0
for i in board.values():
    if i > 1:
        cnt += 1
print(cnt)

