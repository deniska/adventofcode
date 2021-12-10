import sys
import pathlib

lines = pathlib.Path(sys.argv[1]).read_text().strip().split('\n')
nums = []

for line in lines:
    nums.append(int(line))

L = 25

idx = L

def sums(nums):
    for i in nums:
        for j in nums:
            yield i + j

while idx < len(nums):
    if nums[idx] not in sums(nums[idx-L:idx]):
        num = nums[idx]
        print(num)
    idx += 1

i = 0
j = 1
s = nums[i] + nums[j]
while j < len(nums):
    if s < num:
        j += 1
        s += nums[j]
    elif s > num:
        s -= nums[i]
        i += 1
    elif s == num:
        n = max(nums[i:j+1]) + min(nums[i:j+1])
        print(n)
        break
