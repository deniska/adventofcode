import sys
from itertools import product

nums = []
with open(sys.argv[1]) as f:
    for line in f:
        nums.append(int(line))

for i, j in product(nums, nums):
    if i + j == 2020:
        print(i * j)
        break

for i, j, k in product(nums, nums, nums):
    if i + j + k == 2020:
        print(i * j * k)
        break
