import sys
from collections import deque

with open(sys.argv[1]) as f:
    s = f.read().strip()

s_p1, s_p2 = s.split('\n\n')
p1 = deque(int(x) for x in s_p1.split('\n')[1:])
p2 = deque(int(x) for x in s_p2.split('\n')[1:])

while p1 and p2:
    c1 = p1.popleft()
    c2 = p2.popleft()
    if c1 > c2:
        p1.append(c1)
        p1.append(c2)
    else:
        p2.append(c2)
        p2.append(c1)

w = p1 or p2
score = 0
for i, s in enumerate(reversed(w), start=1):
    score += i*s
print(score)
