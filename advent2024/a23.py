import sys

connections = set()
computers = set()

with open(sys.argv[1]) as f:
    for line in f:
        a, b = line.strip().split('-')
        computers.add(a)
        computers.add(b)
        connections.add((a, b))
        connections.add((b, a))

last_groups = {frozenset([a, b]) for (a, b) in connections}
groups = []
while last_groups:
    next_groups = set()
    for group in last_groups:
        for c1 in computers:
            for c2 in group:
                if (c1, c2) not in connections:
                    break
            else:
                next_groups.add(group | {c1})
    last_groups = next_groups
    groups.extend(last_groups)

s = 0
for g in groups:
    if len(g) > 3:
        break
    a, b, c = g
    if a[0] == 't' or b[0] == 't' or c[0] == 't':
        s += 1
print(s)
print(','.join(sorted(groups[-1])))
