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

for _ in range(10):
    last = d[0]
    next_d = [last]
    for c in d[1:]:
        next_d.append(mapping[last+c])
        next_d.append(c)
        last = c
    d = next_d

c = collections.Counter(d)
cc = c.most_common()
print(cc[0][1] - cc[-1][1])
