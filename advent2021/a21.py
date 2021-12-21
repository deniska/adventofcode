import sys

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

s1 = 0
s2 = 0
p1 = p1start
p2 = p2start
die = Die()
while True:
    p1 += die.throw3()
    p1 = (p1 - 1) % 10 + 1
    s1 += p1
    if s1 >= 1000:
        break
    p2 += die.throw3()
    p2 = (p2 - 1) % 10 + 1
    s2 += p2
    if s2 >= 1000:
        break

print(min(s1, s2) * die.rolls)
