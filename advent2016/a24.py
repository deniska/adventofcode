import fileinput
import itertools
import functools

map = []

for line in fileinput.input():
    map.append(line.strip())

def find_biggest():
    m = 0
    for row in map:
        for char in row:
            if char in '0123456789':
                m = max(m, int(char))
    return m

def find_coord(num):
    s = str(num)
    for r, row in enumerate(map):
        for c, char in enumerate(row):
            if char == s:
                return r, c
    raise ValueError('Num {} not found'.format(num))

@functools.lru_cache()
def find_two_points_length(a, b):
    r1, c1 = find_coord(a)
    r2, c2 = find_coord(b)
    return bfs_length(r1, c1, r2, c2)

def neighbours(r, c):
    yield r-1, c
    yield r+1, c
    yield r, c-1
    yield r, c+1

def bfs_length(r1, c1, r2, c2):
    frontier = [(r1, c1)]
    seen = set()
    i = 1
    while True:
        new_frontier = []
        for r, c in frontier:
            for rr, cc in neighbours(r, c):
                try:
                    if map[rr][cc] == '#':
                        continue
                except IndexError:
                    continue
                if (rr, cc) in seen:
                    continue
                if (rr, cc) == (r2, c2):
                    return i
                seen.add((rr, cc))
                new_frontier.append((rr, cc))
        i += 1
        frontier = new_frontier

def possible_paths(biggest):
    for p in itertools.permutations(range(1, biggest+1)):
        yield [0, *p]

def find_path_length(path):
    l = 0
    for p0, p1 in zip(path, path[1:]):
        l += find_two_points_length(p0, p1)
    return l

biggest = find_biggest()
path_lengths = []
for path in possible_paths(biggest):
    l = find_path_length(path)
    path_lengths.append(l)

print(min(path_lengths))

path_lengths = []
for path in possible_paths(biggest):
    l = find_path_length((*path, 0))
    path_lengths.append(l)

print(min(path_lengths))
