import sys
import itertools
import collections

mapping = {}

with open(sys.argv[1]) as f:
    d = list(next(f).strip())
    next(f)
    for line in f:
        a, b = line.strip().split(' -> ')
        mapping[a] = b

polys = collections.Counter()
for a, b in itertools.pairwise(d):
    polys[a+b] += 1

for _ in range(40):
    next_polys = polys.copy()
    for poly, cnt in polys.items():
        next_polys[poly] -= cnt
        x, y = poly
        z = mapping[poly]
        next_polys[x+z] += cnt
        next_polys[z+y] += cnt
    polys = next_polys

c = collections.Counter()
for poly, cnt in polys.items():
    a, b = poly
    c[a] += cnt
    c[b] += cnt
c[d[0]] += 1
c[d[-1]] += 1
for a, cnt in c.items():
    c[a] //= 2

cc = c.most_common()
print(cc[0][1] - cc[-1][1])
