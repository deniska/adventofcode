import sys
from collections import deque

with open(sys.argv[1]) as f:
    s = f.read().strip()

s_p1, s_p2 = s.split('\n\n')
p1 = deque(int(x) for x in s_p1.split('\n')[1:])
p2 = deque(int(x) for x in s_p2.split('\n')[1:])

def part1(p1, p2):
    p1 = p1.copy()
    p2 = p2.copy()
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
    return score

def part2(p1, p2):
    configs = set()
    init_config = (tuple(p1), tuple(p2))
    while p1 and p2:
        config = (tuple(p1), tuple(p2))
        if config in configs:
            return 1, 0
        c1 = p1.popleft()
        c2 = p2.popleft()
        if c1 <= len(p1) and c2 <= len(p2):
            p1s = p1.copy()
            p2s = p2.copy()
            for _ in range(len(p1) - c1):
                p1s.pop()
            for _ in range(len(p2) - c2):
                p2s.pop()
            w, _ = part2(p1s, p2s)
            if w == 1:
                p1.append(c1)
                p1.append(c2)
            else:
                p2.append(c2)
                p2.append(c1)
        else:
            if c1 > c2:
                p1.append(c1)
                p1.append(c2)
            else:
                p2.append(c2)
                p2.append(c1)
        configs.add(config)
    ww = 1 if p1 else 2
    w = p1 or p2
    score = 0
    for i, s in enumerate(reversed(w), start=1):
        score += i*s
    return ww, score

print(part1(p1, p2))
print(part2(p1, p2)[1])
