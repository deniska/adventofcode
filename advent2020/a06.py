import sys

lines = []

with open(sys.argv[1]) as f:
    for line in f:
        lines.append(line.strip())

lines.append('')

group = set()
cnt = 0
for line in lines:
    if not line:
        cnt += len(group)
        group = set()
        continue
    group |= set(line)

print(cnt)

group = set()
first = True
cnt = 0
for line in lines:
    if not line:
        first = True
        cnt += len(group)
        group = set()
        continue
    if first:
        first = False
        group = set(line)
    else:
        group &= set(line)

print(cnt)
