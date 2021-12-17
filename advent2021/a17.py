import sys
import re

with open(sys.argv[1]) as f:
    s = f.read()

m = re.findall(r'-?\d+', s)
x1 = int(m[0])
x2 = int(m[1])
y1 = int(m[2])
y2 = int(m[3])

def sim(vx, vy):
    x = 0
    y = 0
    m = 0
    while True:
        x += vx
        y += vy
        m = max(m, y)
        if vx > 0:
            vx -= 1
        vy -= 1
        if x > x2 or y < y1:
            return None
        if x1 <= x <= x2 and y1 <= y <= y2:
            return m

def go():
    m = 0
    c = 0
    for vx in range(1000):
        for vy in range(-1000, 1000):
            s = sim(vx, vy)
            if s is not None:
                c += 1
                m = max(m, s)
    print(m)
    print(c)

go()
