import re
import attr
@attr.s
class Node:
    name = attr.ib()
    size = attr.ib()
    used = attr.ib()
    avail = attr.ib()

nodes = []
node_coord = {}
with open('input22.txt') as f:
    next(f)
    next(f)
    for line in f:
        parts = line.strip().split()
        name = parts[0]
        m = re.match(r'/dev/grid/node-x(\d+)-y(\d+)', name)
        coord = (int(m.group(1)), int(m.group(2)))
        size, used, avail = [int(x.strip('T%')) for x in parts[1:4]]
        node = Node(name=name, size=size, used=used, avail=avail)
        nodes.append(node)
        node_coord[coord] = node

c = 0
for n1 in nodes:
    for n2 in nodes:
        if n1 is n2 or n1.used == 0 or n1.used > n2.avail:
            continue
        c += 1
print(c)
width, height = max(node_coord.keys())
width += 1
height += 1
print(width, height)

for y in range(height):
    for x in range(width):
        if (x, y) == (0, 0):
            c = 'x'
        elif node_coord[x, y].used == 0:
            c = '_'
        elif node_coord[x, y].used >= 100:
            c = '#'
        elif (x, y) == (width-1, 0):
            c = 'G'
        else:
            c = '.'
        print(c, end='')
    print()
