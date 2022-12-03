import sys
import string

values = {}
for i, c in enumerate(string.ascii_lowercase, start=1):
    values[c] = i

for i, c in enumerate(string.ascii_uppercase, start=27):
    values[c] = i

data = []
with open(sys.argv[1]) as f:
    for line in f:
        data.append(line.strip())

rucksacks = []
for d in data:
    a = d[:len(d)//2]
    b = d[len(d)//2:]
    rucksacks.append((a, b))

v = 0
for a, b in rucksacks:
    l = set(a) & set(b)
    assert len(l) == 1
    l = l.pop()
    v += values[l]

print(v)

v = 0

for i in range(len(data)//3):
    c = set(data[i*3]) & set(data[i*3+1]) & set(data[i*3+2])
    assert len(c) == 1
    c = c.pop()
    v += values[c]

print(v)
