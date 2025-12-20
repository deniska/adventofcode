import re
import sys
import itertools

ingrs = []

with open(sys.argv[1]) as f:
    for line in f:
        nums = [int(num) for num in re.findall(r'-?\d+', line)]
        ingrs.append(nums)

p1 = 0
p2 = 0
for ingr_counts in itertools.product(*[range(101)]*len(ingrs)):
    if sum(ingr_counts) > 100:
        continue
    score = 1
    for i in range(4):
        score *= max(0, sum(ingr[i] * ingr_count for (ingr, ingr_count) in zip(ingrs, ingr_counts)))
    calories = sum(ingr[4] * ingr_count for (ingr, ingr_count) in zip(ingrs, ingr_counts))
    if score > p1:
        p1 = score
    if calories == 500 and score > p2:
        p2 = score

print(p1)
print(p2)
