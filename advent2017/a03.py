def coords():
    d = 'right'
    i = 1
    x, y = 0, 0
    steps = 2
    while True:
        for _ in range(steps//2):
            yield x, y, i
            x = {'right': x+1, 'left': x-1, 'up': x, 'down': x}[d]
            y = {'right': y, 'left': y, 'up': y+1, 'down': y-1}[d]
            i += 1
        steps += 1
        d = {'up': 'left', 'left': 'down', 'down': 'right', 'right': 'up'}[d]

spiral_coords = []
d = {}
for x, y, i in coords():
    #print(i, x, y)
    spiral_coords.append((x, y))
    d[x, y] = 0
    if i >= 289326:
        print(abs(x) + abs(y))
        break

d[0, 0] = 1
for x, y in spiral_coords[1:]:
    d[x, y] = d[x-1, y-1] + d[x, y-1] + d[x+1, y-1] + d[x-1, y] + d[x+1, y] + d[x-1, y+1] + d[x, y+1] + d[x+1, y+1]
    if d[x, y] > 289326:
        print(d[x, y])
        break
