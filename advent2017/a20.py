import re
from collections import Counter
pos = []
vel = []
acc = []

with open('input20.txt') as f:
    for line in f:
        m = re.findall(r'-?\d+', line)
        pos.append((int(m[0]), int(m[1]), int(m[2])))
        vel.append((int(m[3]), int(m[4]), int(m[5])))
        acc.append((int(m[6]), int(m[7]), int(m[8])))

for i in range(10000):
    cpos = Counter(pos)
    todel = []
    for i, p in enumerate(pos):
        if cpos[p] > 1:
            todel.append(i)
    for i in reversed(todel):
        del pos[i]
        del vel[i]
        del acc[i]
    vel = [(v[0] + a[0], v[1] + a[1], v[2] + a[2]) for v, a in zip(vel, acc)]
    pos = [(p[0] + v[0], p[1] + v[1], p[2] + v[2]) for p, v in zip(pos, vel)]

dists = []
for p in pos:
    dists.append(abs(p[0]) + abs(p[1]) + abs(p[2]))

print(len(pos))
print(min((v, i) for i, v in enumerate(dists)))

