import sys
import pathlib
import functools

lines = pathlib.Path(sys.argv[1]).read_text().strip().split('\n')
nums = []

for line in lines:
    nums.append(int(line))

chain = sorted(nums)
prev = 0

ones = 0
threes = 1 # the device is always 3 jolts apart
for num in chain:
    if num - prev == 1:
        ones += 1
    elif num - prev == 3:
        threes += 1
    prev = num

print(ones * threes)

@functools.lru_cache(maxsize=None)
def part2(prev=0, idx=0):
    if len(chain) <= idx:
        return 0
    if chain[idx] - prev > 3:
        return 0
    if idx == len(chain) - 1:
        return 1
    prev = chain[idx]
    return part2(prev, idx+1) + part2(prev, idx+2) + part2(prev, idx+3)

print(part2() + part2(idx=1) + part2(idx=2))
