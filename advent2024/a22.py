import sys
import itertools

buyers = []
with open(sys.argv[1]) as f:
    for line in f:
        buyers.append(int(line.strip()))

def generator(secret):
    while True:
        secret ^= secret * 64
        secret %= 16777216
        secret ^= secret // 32
        secret %= 16777216
        secret ^= secret * 2048
        secret %= 16777216
        yield secret

gs = [generator(b) for b in buyers]
prices = [[b % 10] for b in buyers]
for _ in range(2000):
    nums = [next(g) for g in gs]
    for i, n in enumerate(nums):
        prices[i].append(n % 10)

print(sum(nums)) # part 1

changes = [[] for _ in buyers]
for i, prc in enumerate(prices):
    for a, b in itertools.pairwise(prc):
        changes[i].append(b - a)

combos = [{} for _ in buyers]
for i, change in enumerate(changes):
    for j in range(4, len(change)):
        prev = (change[j-4], change[j-3], change[j-2], change[j-1])
        combos[i].setdefault(prev, prices[i][j])

all_combos = set(combos[0].keys())
for combo in combos:
    all_combos |= combo.keys()

bananas = []
for seq in all_combos:
    s = 0
    for combo in combos:
        s += combo.get(seq, 0)
    bananas.append(s)

print(max(bananas)) # part 2
