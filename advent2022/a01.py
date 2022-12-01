import sys

with open(sys.argv[1]) as f:
    data = f.read()

data = data.split('\n\n')
groups = []
for d in data:
    groups.append([int(x) for x in d.split()])

sums = [sum(g) for g in groups]
print(max(sums))

sums.sort()
print(sum(sums[-3:]))
