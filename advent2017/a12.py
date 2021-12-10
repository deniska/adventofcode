from collections import defaultdict
from itertools import count

connections = defaultdict(list)
nodes = set()
with open('input12.txt') as f:
    for line in f:
        confrom, _, *conto = line.split()
        confrom = int(confrom)
        nodes.add(confrom)
        conto = [int(c.strip(',')) for c in conto]
        for c in conto:
            connections[c].append(confrom)
            connections[confrom].append(c)
            nodes.add(c)

def is_con_to(name, seen=None, val=0):
    if name == val:
        return True
    if seen is None:
        seen = set()
    seen.add(name)
    for conn in connections[name]:
        if conn in seen:
            continue
        if conn == val:
            return True
        if is_con_to(conn, seen, val):
            return True
    return False

i = 0
for n in nodes:
    if is_con_to(n):
        i += 1
print(i)

ns = list(nodes)
j = 0
while ns:
    j += 1
    n = ns.pop()
    for a in list(ns):
        if is_con_to(n, None, a):
            ns.remove(a)
print(j)
