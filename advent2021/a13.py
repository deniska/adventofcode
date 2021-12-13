import sys

dots = set()
folds = []

with open(sys.argv[1]) as f:
    for line in f:
        line = line.strip()
        if not line:
            break
        x, y = line.split(',')
        dots.add((int(x), int(y)))
    for line in f:
        line = line.strip()
        a, b = line.split('=')
        if 'x' in a:
            z = 'x'
        elif 'y' in a:
            z = 'y'
        folds.append((z, int(b)))

for i, (axis, coord) in enumerate(folds):
    new_dots = set()
    if axis == 'x':
        for x, y in dots:
            if x < coord:
                new_dots.add((x, y))
            else:
                new_dots.add((coord*2 - x, y))
    else:
        for x, y in dots:
            if y < coord:
                new_dots.add((x, y))
            else:
                new_dots.add((x, coord*2 - y))
    dots = new_dots
    if i == 0:
        print(len(dots))

print('X\tY')
for x, y in dots:
    print(f'{x}\t{-y}')
