import itertools
import sys

dists = {}
cities = set()

with open(sys.argv[1]) as f:
    for line in f:
        a, _, b, _, d = line.split()
        cities.add(a)
        cities.add(b)
        dists[a, b] = int(d)
        dists[b, a] = int(d)

p1 = 9999999999
p2 = 0
for path in itertools.permutations(cities):
    d = 0
    for i in range(len(path) - 1):
        d += dists[path[i], path[i + 1]]
    if d < p1:
        p1 = d
    if d > p2:
        p2 = d

print(p1)
print(p2)
