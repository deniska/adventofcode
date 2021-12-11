import sys

def main():
    grid = Grid(10, 10)
    with open(sys.argv[1]) as f:
        for y, line in enumerate(f):
            for x, c in enumerate(line.strip()):
                grid[x, y] = int(c)
    flashes = 0
    step_n = 0
    while True:
        f = step(grid)
        flashes += f
        step_n += 1
        if step_n == 100:
            print('Part 1:', flashes)
        if f == 100:
            print('Part 2:', step_n)
            break

def step(grid):
    flashed = set()
    for x, y in grid.everything():
        grid[x, y] += 1
    while True:
        no_new_flashes = True
        for x, y in grid.everything():
            if grid[x, y] > 9 and (x, y) not in flashed:
                no_new_flashes = False
                flashed.add((x, y))
                for x1, y1 in grid.neightbours(x, y):
                    grid[x1, y1] += 1
        if no_new_flashes:
            break
    for x, y in flashed:
        grid[x, y] = 0
    return len(flashed)


class Grid:

    def __init__(self, w, h):
        self.w = w
        self.h = h
        self.data = [0] * (w * h)

    def _checkrange(self, x, y):
        if not (0 <= x < self.w):
            raise IndexError(f'{x=} not in range')
        if not (0 <= y < self.h):
            raise IndexError(f'{y=} not in range')

    def __getitem__(self, a):
        x, y = a
        self._checkrange(x, y)
        return self.data[y * self.w + x]
    
    def __setitem__(self, a, v):
        x, y = a
        self._checkrange(x, y)
        self.data[y * self.w + x] = v

    def neightbours(self, x, y):
        self._checkrange(x, y)
        for i in (-1, 0, 1):
            for j in (-1, 0, 1):
                if i == 0 and j == 0:
                    continue
                xx = x + i
                yy = y + j
                try:
                    self._checkrange(xx, yy)
                except IndexError:
                    continue
                yield xx, yy

    def everything(self):
        for j in range(self.h):
            for i in range(self.w):
                yield i, j

    def __str__(self):
        lines = []
        for y in range(self.h):
            line = []
            for x in range(self.w):
                line.append(str(self[x, y]))
            lines.append(''.join(line))
        return '\n'.join(lines)

if __name__ == '__main__':
    main()
