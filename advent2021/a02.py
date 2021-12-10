import sys

with open(sys.argv[1]) as f:
    lines = f.read().strip().split('\n')

cmds = []
for line in lines:
    cmd, n = line.split()
    n = int(n)
    cmds.append((cmd, n))

depth = 0
hor = 0

for cmd, n in cmds:
    if cmd == 'forward':
        hor += n
    elif cmd == 'up':
        depth -= n
    elif cmd == 'down':
        depth += n

print(depth * hor)

depth = 0
hor = 0
aim = 0

for cmd, n in cmds:
    if cmd == 'down':
        aim += n
    elif cmd == 'up':
        aim -= n
    elif cmd == 'forward':
        hor += n
        depth += aim * n

print(depth * hor)
