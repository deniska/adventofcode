import sys
from collections import Counter
from itertools import product

with open(sys.argv[1]) as f:
    p1start = int(next(f).rpartition(' ')[2].strip())
    p2start = int(next(f).rpartition(' ')[2].strip())

class Die:

    def __init__(self):
        self.n = 1
        self.rolls = 0
    
    def throw(self):
        n = self.n
        self.n += 1
        if self.n > 100:
            self.n = 1
        self.rolls += 1
        return n

    def throw3(self):
        return self.throw() + self.throw() + self.throw()

def boardpos(n):
    return (n - 1) % 10 + 1

def part1():
    s1 = 0
    s2 = 0
    p1 = p1start
    p2 = p2start
    die = Die()
    while True:
        p1 += die.throw3()
        p1 = boardpos(p1)
        s1 += p1
        if s1 >= 1000:
            break
        p2 += die.throw3()
        p2 = boardpos(p2)
        s2 += p2
        if s2 >= 1000:
            break

    return min(s1, s2) * die.rolls

def gen_q3d3():
    c = Counter()
    for i, j, k in product(*[range(1, 4)]*3):
        c[i+j+k] += 1
    return c

def part2():
    s1 = 0
    s2 = 0
    p1 = p1start
    p2 = p2start
    states = Counter({(s1, p1, s2, p2): 1})
    win_states = Counter()
    q3d3 = gen_q3d3()
    while states:
        next_states = Counter()
        for (s1, p1, s2, p2), cnt in states.items():
            for i, m in q3d3.items():
                p1n = boardpos(p1 + i)
                s1n = s1 + p1n
                if s1n >= 21:
                    win_states[s1n, p1n, s2, p2] += cnt * m
                else:
                    next_states[s1n, p1n, s2, p2] += cnt * m
        states = next_states
        next_states = Counter()
        for (s1, p1, s2, p2), cnt in states.items():
            for i, m in q3d3.items():
                p2n = boardpos(p2 + i)
                s2n = s2 + p2n
                if s2n >= 21:
                    win_states[s1, p1, s2n, p2n] += cnt * m
                else:
                    next_states[s1, p1, s2n, p2n] += cnt * m
        states = next_states
    wins1 = 0
    wins2 = 0
    for (s1, p2, s2, p2), cnt in win_states.items():
        if s1 >= 21:
            wins1 += cnt
        else:
            wins2 += cnt
    return max(wins1, wins2)

print(part1())
print(part2())
