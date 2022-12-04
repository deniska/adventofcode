import sys

v = 0
u = 0

with open(sys.argv[1]) as f:
    for line in f:
        x, y = line.strip().split(',')
        a, b = x.split('-')
        c, d = y.split('-')
        a = int(a)
        b = int(b)
        c = int(c)
        d = int(d)
        if (a <= c and b >= d
                or c <= a and d >= b):
            v += 1
        if (a <= c <= b
                or a <= d <= b
                or c <= a <= d
                or c <= b <= d):
            u += 1

print(v)
print(u)
