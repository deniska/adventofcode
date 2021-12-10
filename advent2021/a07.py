import sys

with open(sys.argv[1]) as f:
    ns = [int(n) for n in f.read().strip().split(',')]

def check(x):
    return sum(abs(n - x) for n in ns)

def check2(x):
    s = 0
    for n in ns:
        d = abs(n - x)
        f = d*(d+1) // 2
        s += f
    return s

def part1():
    return min(check(x) for x in range(min(ns), max(ns)+1))

def part2():
    return min(check2(x) for x in range(min(ns), max(ns)+1))

print(part1())
print(part2())
