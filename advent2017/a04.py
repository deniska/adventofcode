from collections import Counter

with open('input04.txt') as f:
    lines = f.readlines()

def anawords(words):
    counters = [Counter(w) for w in words]
    for i, c1 in enumerate(counters):
        for c2 in counters[i+1:]:
            if c1 == c2:
                return True
    return False

i = 0
j = 0
for line in lines:
    words = line.split()
    if len(words) == len(set(words)):
        i += 1
    if not anawords(words):
        j += 1
print(i)
print(j)
