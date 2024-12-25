import sys

locks = []
keys = []

with open(sys.argv[1]) as f:
    data = f.read()

for thing in data.split('\n\n'):
    parsed = [-1] * 5
    for line in thing.splitlines():
        for i, c in enumerate(line):
            if c == '#':
                parsed[i] += 1
    if thing[0] == '#':
        locks.append(parsed)
    elif thing[0] == '.':
        keys.append(parsed)

cnt = 0
for lock in locks:
    for key in keys:
        for a, b in zip(lock, key):
            if a + b > 5:
                break
        else:
            cnt += 1
print(cnt)
