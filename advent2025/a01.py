import re
import sys

q = 50
p1 = 0
p2 = 0

with open(sys.argv[1]) as f:
    for line in f:
        m = re.match(r'([LR])(\d+)', line)
        d = 1 if m[1] == 'R' else -1
        n = int(m[2])

        for _ in range(n):
            q += d
            q %= 100
            if q == 0:
                p2 += 1

        if q == 0:
            p1 += 1

print(p1)
print(p2)
