import sys

def tail_should_move(a, b):
    return abs(a[0] - b[0]) > 1 or abs(a[1] - b[1]) > 1

tail = (0, 0)
head = (0, 0)
prev_head = (0, 0)
dirs = {
    'R': (1, 0),
    'L': (-1, 0),
    'U': (0, 1),
    'D': (0, -1),
}
positions = {tail}

with open(sys.argv[1]) as f:
    for line in f:
        line = line.strip()
        d, c = line.split()
        c = int(c)
        dx, dy = dirs[d]
        for i in range(c):
            prev_head = head
            head = (head[0] + dx, head[1] + dy)
            if tail_should_move(head, tail):
                tail = prev_head
                positions.add(tail)

print(len(positions))
