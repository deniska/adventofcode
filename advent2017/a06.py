blocks = [4, 1, 15, 12, 0, 9, 9, 5, 5, 8, 7, 3, 14, 5, 12, 3]
seen = {tuple(blocks)}
z = 0
while True:
    z += 1
    maxind, maxval = max(enumerate(blocks), key=lambda x: (x[1], -x[0]))
    blocks[maxind] = 0
    for i in range(maxval):
        blocks[(maxind+i+1) % len(blocks)] += 1
    t = tuple(blocks)
    if t in seen:
        print(z)
        break
    seen.add(t)

z = 0
while True:
    z += 1
    maxind, maxval = max(enumerate(blocks), key=lambda x: (x[1], -x[0]))
    blocks[maxind] = 0
    for i in range(maxval):
        blocks[(maxind+i+1) % len(blocks)] += 1
    if t == tuple(blocks):
        break
print(z)
