import re
import sys
import itertools
import operator

calibs = []

with open(sys.argv[1]) as f:
    for line in f:
        calibs.append([int(x) for x in re.findall(r'\d+', line)])

ops = [operator.add, operator.mul]
ops1 = ops + [lambda x, y: int(str(x) + str(y))]

def is_valid(calib, ops):
    s, num0, *nums = calib
    for p in itertools.product(*[ops]*(len(nums))):
        r = num0
        for o, n in zip(p, nums):
            r = o(r, n)
        if r == s:
            return True
    return False

s = 0
for calib in calibs:
    if is_valid(calib, ops):
        s += calib[0]
print(s)

s = 0
for calib in calibs:
    if is_valid(calib, ops1):
        s += calib[0]
print(s)
