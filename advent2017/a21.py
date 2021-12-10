import numpy as np

def get_rules(s):
    rules = {}
    for line in s.splitlines():
        a, b = line.split(' => ')
        rules[a] = str_to_arr(b.strip().replace('/', '\n'))
    return rules

def new_grid(grid):
    dim = grid.shape[0]
    if dim % 2 == 0:
        step = 2
    else:
        step = 3
    sub_cols = np.hsplit(grid, dim // step)
    new_cols = []
    for sub_col in sub_cols:
        subs = np.vsplit(sub_col, dim // step)
        new_subs = []
        for sub in subs:
            new_sub = find_rule(sub)
            new_subs.append(new_sub)
        new_cols.append(np.concatenate(new_subs, 0))
    return np.concatenate(new_cols, 1)

def arr_to_str(a):
    parts = [''.join('#' if x else '.' for x in a[i,:]) for i in range(a.shape[0])]
    return '\n'.join(parts)

def str_to_arr(a):
    a = a.splitlines()
    arr = np.zeros((len(a), len(a)), np.int32)
    for i, line in enumerate(a):
        for j, c in enumerate(line):
            if c == '#':
                arr[i, j] = 1
    return arr

def variants(arr):
    yield from flips(arr)
    for i in range(3):
        arr = np.rot90(arr)
        yield from flips(arr)

def flips(arr):
    yield arr
    yield np.flipud(arr)
    yield np.fliplr(arr)


def find_rule(arr):
    for variant in variants(arr):
        var_str = arr_to_str(variant).replace('\n', '/')
        if var_str in rules:
            return rules[var_str]

with open('input21.txt') as f:
    rules = get_rules(f.read())

#rules = get_rules('''../.# => ##./#../...
#.#./..#/### => #..#/..../..../#..#''')

grid = np.array([[0, 1, 0], [0, 0, 1], [1, 1, 1]], np.int32)

for i in range(18):
    grid = new_grid(grid)
    print(i+1, np.count_nonzero(grid))
