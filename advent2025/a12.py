import sys

shapes = []

p1 = 0

with open(sys.argv[1]) as f:
    for line in f:
        first, _, second = line.strip().partition(':')
        if not second:
            shape = 0
            while True:
                line = next(f).strip()
                if not line:
                    break
                shape += line.count('#')
            shapes.append(shape)
        else:
            a, b = first.split('x')
            a = int(a)
            b = int(b)
            shape_counts = [int(c) for c in second.split()]
            sq = sum(shapes[i] * shape_counts[i] for i in range(len(shapes)))
            if sq < a*b:
                p1 += 1

print(p1)
