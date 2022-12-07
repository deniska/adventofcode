import sys
import functools
import collections

sizes = collections.Counter()
sizes['/'] = 0

with open(sys.argv[1]) as f:
    for line in f:
        line = line.strip()
        if line == '$ cd /':
            cur_path = '/'
        elif line == '$ cd ..':
            cur_path = cur_path.rpartition('/')[0]
            if len(cur_path) == 0:
                cur_path = '/'
        elif line.startswith('$ cd'):
            d = line.rpartition(' ')[2]
            if len(cur_path) > 1:
                cur_path += f'/{d}'
            else:
                cur_path += d
            if cur_path not in sizes:
                sizes[cur_path] = 0
        elif line == '$ ls':
            continue
        else:
            size, name = line.split()
            if size == 'dir':
                continue
            sizes[cur_path] += int(size)

total_sizes = collections.Counter()

for path in sizes.keys():
    for k, v in sizes.items():
        if k.startswith(path):
            total_sizes[path] += v

p1 = 0
for k, v in total_sizes.items():
    if v <= 100000:
        p1 += v

print(p1)

to_free = 30000000 - (70000000 - total_sizes['/'])
print(min(v for v in total_sizes.values() if v >= to_free))
