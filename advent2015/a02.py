import sys

a = 0
r = 0

with open(sys.argv[1]) as f:
    for line in f:
        line = line.strip()
        l, w, h = [int(q) for q in line.split('x')]
        a += 2*l*w + 2*w*h + 2*h*l + min(l*w, w*h, h*l)
        r += 2*min(l+w, w+h, h+l) + w*h*l

print(a)
print(r)
