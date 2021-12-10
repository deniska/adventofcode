import sys
import pathlib
import functools
from itertools import product

lines = pathlib.Path(sys.argv[1]).read_text().strip().split('\n')

cmds = []

for line in lines:
    cmd, param = line[0], int(line[1:])
    cmds.append((cmd, param))

x, y = (0, 0)
d = {
        'E': (1, 0),
        'N': (0, 1),
        'W': (-1, 0),
        'S': (0, -1),
        }
dirs = ['E', 'N', 'W', 'S']
cur_dir = 0

for cmd, param in cmds:
    if cmd in d:
        dx, dy = d[cmd]
        x += dx * param
        y += dy * param
    elif cmd in 'RL':
        c = param // 90
        if cmd == 'R':
            c *= -1
        cur_dir += c
        cur_dir %= 4
    elif cmd == 'F':
        dx, dy = d[dirs[cur_dir]]
        x += dx * param
        y += dy * param
print(abs(x) + abs(y))

wx, wy = 10, 1
x, y = 0, 0

for cmd, param in cmds:
    if cmd in d:
        dx, dy = d[cmd]
        wx += dx * param
        wy += dy * param
    elif cmd in 'RL':
        z = 1
        if cmd == 'R':
            z = -1
        c = param // 90
        for _ in range(c):
            wx, wy = -wy * z, wx * z
    elif cmd == 'F':
        x += wx * param
        y += wy * param
print(abs(x) + abs(y))
