import sys
import itertools

data = {}
people = set()

with open(sys.argv[1]) as f:
    for line in f:
        parts = line.strip('\r\n.').split()
        a = parts[0]
        b = parts[-1]
        n = int(parts[3])
        if parts[2] == 'lose':
            n = -n
        data[a, b] = n
        people.add(a)
        people.add(b)

def solve():
    res = 0
    for arrangement in itertools.permutations(people):
        h = 0
        for i in range(len(arrangement)):
            h += data.get((arrangement[i], arrangement[(i+1) % len(arrangement)]), 0)
            h += data.get((arrangement[i], arrangement[i-1]), 0)
        if h > res:
            res = h
    return res

p1 = solve()
print(p1)
people.add('me')
p2 = solve()
print(p2)
