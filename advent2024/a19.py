import re
import sys

designs = []
with open(sys.argv[1]) as f:
    towels = f.readline().strip().split(', ')
    f.readline()
    for line in f:
        designs.append(line.strip())

towels.sort(key=lambda x: (len(x), x))

def towels_regexp(towels):
    regexp = '({})+'.format('|'.join(towels))
    return regexp

optimized_towels = [towels[0]]
for t in towels[1:]:
    if not re.fullmatch(towels_regexp(optimized_towels), t):
        optimized_towels.append(t)

regexp = towels_regexp(optimized_towels)

c = 0
for d in designs:
    if re.fullmatch(regexp, d):
        c += 1

print(c)
