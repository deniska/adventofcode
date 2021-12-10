import sys
from itertools import pairwise

with open(sys.argv[1]) as f:
    s = f.read()

nums = [int(a) for a in s.split()]

count = 0
for n1, n2 in pairwise(nums):
    if n2 > n1:
        count += 1
print(count)

count = 0
windows = [nums[i:i+3] for i in range(len(nums)-2)]
for w1, w2 in pairwise(windows):
    if sum(w2) > sum(w1):
        count += 1
print(count)
