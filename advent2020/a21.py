import sys
import collections

lines = []

with open(sys.argv[1]) as f:
    for line in f:
        a1, a2 = line.strip().split(' (contains ')
        ingredients = set(a1.split())
        allergens = set(s.strip(',)') for s in a2.split())
        lines.append((ingredients, allergens))

have_allergens = set()
for i, (i1, a1) in enumerate(lines):
    i1 = i1.copy()
    for j, (i2, a2) in enumerate(lines):
        if i == j:
            continue
        if a1 & a2:
            i1 &= i2
    have_allergens |= i1

c = 0
for i1, a1 in lines:
    for i in i1:
        if i not in have_allergens:
            c += 1
print(c)
