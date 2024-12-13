import re
import sys

rgx = r'''Button A: X\+(\d+), Y\+(\d+)
Button B: X\+(\d+), Y\+(\d+)
Prize: X=(\d+), Y=(\d+)
'''

with open(sys.argv[1]) as f:
    txt = f.read()

machines = []
for machine in re.findall(rgx, txt):
    machines.append([int(x) for x in machine])

s = 0
for machine in machines:
    ax, ay, bx, by, px, py = machine
    a = (-bx*py + by*px)/(ax*by - ay*bx)
    b = (ax*py - ay*px)/(ax*by - ay*bx)
    if a.is_integer() and b.is_integer():
        s += int(a) * 3 + int(b)
print(s)

s = 0
for machine in machines:
    ax, ay, bx, by, px, py = machine
    px += 10000000000000
    py += 10000000000000
    a = (-bx*py + by*px)/(ax*by - ay*bx)
    b = (ax*py - ay*px)/(ax*by - ay*bx)
    if a.is_integer() and b.is_integer():
        s += int(a) * 3 + int(b)
print(s)
