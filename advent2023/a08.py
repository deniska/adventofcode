import sys
import math
import itertools

m = {}

with open(sys.argv[1]) as f:
    ins = next(f).strip()
    next(f)
    for line in f:
        a = line[0:3]
        b = line[7:10]
        c = line[12:15]
        m[a] = (b, c)

cur = 'AAA'
cnt = 0
for d in itertools.cycle(ins):
    if d == 'L':
        cur = m[cur][0]
    else:
        cur = m[cur][1]
    cnt += 1
    if cur == 'ZZZ':
        break
print(cnt)


cursors = [k for k in m if k.endswith('A')]
cnt = 0
first = {}
second = {}
for d in itertools.cycle(ins):
    for i, cur in enumerate(cursors):
        if d == 'L':
            cursors[i] = m[cur][0]
        else:
            cursors[i] = m[cur][1]
    cnt += 1
    for i, cur in enumerate(cursors):
        if cur.endswith('Z'):
            if i not in first:
                first[i] = cnt
            elif i not in second:
                second[i] = cnt
    if len(second) == len(cursors):
        break
periods = [second[i] - first[i] for i in range(len(cursors))]
for i, p in enumerate(periods):
    if first[i] != p:
        raise Exception('Oh no')

print(math.lcm(*periods))
