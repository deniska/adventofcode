import sys
from collections import defaultdict

m = defaultdict(list)

with open(sys.argv[1]) as f:
    for line in f:
        line = line.strip()
        a, b = line.split('-')
        m[a].append(b)
        m[b].append(a)

def traverse(path, seen):
    if path[-1] == 'end':
        return 1
    s = 0
    for cave in m[path[-1]]:
        if cave in seen:
            continue
        if cave.lower() == cave:
            seen1 = {*seen, cave}
        else:
            seen1 = seen
        s += traverse([*path, cave], seen1)
    return s

def traverse2(path, seen, seen_twice=False):
    if path[-1] == 'end':
        return 1
    s = 0
    for cave in m[path[-1]]:
        seen_twice1 = seen_twice
        if cave == 'start':
            continue
        if cave in seen and seen_twice:
            continue
        elif cave in seen and not seen_twice:
            seen_twice1 = True
        if cave.lower() == cave:
            seen1 = {*seen, cave}
        else:
            seen1 = seen
        s += traverse2([*path, cave], seen1, seen_twice1)
    return s

print(traverse(['start'], {'start'}))
print(traverse2(['start'], {'start'}))
