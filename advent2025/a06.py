import sys

nums = []

with open(sys.argv[1]) as f:
    for line in f:
        things = line.split()
        try:
            nums.append([int(t) for t in things])
        except ValueError:
            ops = things

p1 = 0
for problem_idx in range(len(nums[0])):
    op = ops[problem_idx]
    if op == '+':
        res = 0
    else:
        res = 1
    for num_idx in range(len(nums)):
        if op == '+':
            res += nums[num_idx][problem_idx]
        else:
            res *= nums[num_idx][problem_idx]
    p1 += res

print(p1)
