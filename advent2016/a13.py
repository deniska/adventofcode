favnum = 1350

def is_wall(x, y):
    n = x*x + 3*x + 2*x*y + y + y*y + favnum
    s = 0
    while n > 0:
        s += n & 1
        n = n >> 1
    return s % 2 == 1


for y in range(50):
    for x in range(50):
        if is_wall(x, y):
            c = '#'
        elif x == 31 and y == 39:
            c = 'X'
        else:
            c = ' '
        print(c, end='')
    print()

movements = [(-1, 0), (0, -1), (1, 0), (0, 1)]
def search():
    frontier = [(1,1)]
    checked = {(1, 1)}
    i = 0
    while not (31, 39) in checked:
        next_frontier = []
        for x, y in frontier:
            for dx, dy in movements:
                xx = x + dx
                yy = y + dy
                if xx < 0 or yy < 0 or (xx, yy) in checked or is_wall(xx, yy):
                    continue
                checked.add((xx, yy))
                next_frontier.append((xx, yy))
        frontier = next_frontier
        i += 1
        if i == 50:
            print(len(checked))
    print(i)

search()

