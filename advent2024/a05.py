import sys
import collections

rules = collections.defaultdict(set)
updates = []

with open(sys.argv[1]) as f:
    for line in f:
        line = line.strip()
        if not line:
            break
        n1, n2 = line.split('|')
        n1 = int(n1)
        n2 = int(n2)
        rules[n2].add(n1)
    for line in f:
        line = line.strip()
        updates.append([int(x) for x in line.split(',')])

def is_valid(update):
    for i in range(len(update) - 1):
        for j in range(i + 1, len(update)):
            if update[j] in rules[update[i]]:
                return False, j
    return True, -1

s = 0
incorrect = []
for update in updates:
    if is_valid(update)[0]:
        s += update[len(update) // 2]
    else:
        incorrect.append(update)
print(s)

s = 0
for update in incorrect:
    while (i := is_valid(update)[1]) >= 0:
        update[i - 1], update[i] = update[i], update[i - 1]
    s += update[len(update) // 2]
print(s)
