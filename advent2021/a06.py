import sys

with open(sys.argv[1]) as f:
    ns = [int(n) for n in f.read().strip().split(',')]

class Lanternfish:

    def __init__(self, n):
        self.n = n

    def cycle(self):
        if self.n == 0:
            self.n = 6
            return True
        else:
            self.n -= 1
            return False


fish = [Lanternfish(n) for n in ns]
for days in range(80):
    next_fish = fish.copy()
    for f in fish:
        if f.cycle():
            next_fish.append(Lanternfish(8))
    fish = next_fish

print(len(next_fish))
