import sys
import itertools

dirs = {
    'R': (1, 0),
    'L': (-1, 0),
    'U': (0, 1),
    'D': (0, -1),
}

def cmp(a, b):
    if a > b:
        return 1
    elif a == b:
        return 0
    else:
        return -1

class Knot:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.px = 0
        self.py = 0

    def move_cmd(self, d):
        dx, dy = dirs[d]
        self.x += dx
        self.y += dy

    def follow(self, another):
        if abs(self.x - another.x) <= 1 and abs(self.y - another.y) <= 1:
            return
        dx = cmp(another.x, self.x)
        dy = cmp(another.y, self.y)
        self.x += dx
        self.y += dy

    def pos(self):
        return self.x, self.y

rope = [Knot() for _ in range(10)]
the_tail = rope[-1]
positions = {the_tail.pos()}

with open(sys.argv[1]) as f:
    for line in f:
        line = line.strip()
        d, c = line.split()
        c = int(c)
        for i in range(c):
            rope[0].move_cmd(d)
            for head, tail in itertools.pairwise(rope):
                tail.follow(head)
            positions.add(the_tail.pos())

print(len(positions))
