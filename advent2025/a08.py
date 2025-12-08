import sys
import collections

boxes = []

with open(sys.argv[1]) as f:
    for line in f:
        x, y, z = line.strip().split(',')
        boxes.append((int(x), int(y), int(z)))

nets = list(range(len(boxes)))
cnt_nets = len(boxes)
dists = []

for i, (x1, y1, z1) in enumerate(boxes):
    for j, (x2, y2, z2) in enumerate(boxes):
        if i >= j: continue
        dists.append(((x1 - x2)**2 + (y1 - y2)**2 + (z1 - z2)**2, i, j))

dists.sort()

cons = 0
for _, i, j in dists:
    if (m := nets[i]) != (n := nets[j]):
        for k, net in enumerate(nets):
            if nets[k] == m:
                nets[k] = n
        cnt_nets -= 1
    cons += 1
    if cons == 1000:
        p1 = 1
        for _, c in collections.Counter(nets).most_common(3):
            p1 *= c
        print(p1)
    if cnt_nets == 1:
        p2 = boxes[i][0] * boxes[j][0]
        print(p2)
        break
