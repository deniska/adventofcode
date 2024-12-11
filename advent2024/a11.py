import sys
import collections

with open(sys.argv[1]) as f:
    stones = collections.Counter([int(s) for s in f.read().split()])

def blink(stones):
    new_stones = collections.Counter()
    for stone, count in stones.items():
        if stone == 0:
            new_stones[1] += count
        elif len(s := str(stone)) % 2 == 0:
            l = len(s) // 2
            new_stones[int(s[:l])] += count
            new_stones[int(s[l:])] += count
        else:
            new_stones[stone * 2024] += count
    return new_stones

for _ in range(25):
    stones = blink(stones)
print(sum(stones.values()))

for _ in range(75 - 25):
    stones = blink(stones)
print(sum(stones.values()))

