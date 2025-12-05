import sys

ranges = []
nums = []

with open(sys.argv[1]) as f:
    for line in f:
        line = line.strip()
        if not line:
            break
        a, b = line.split('-')
        ranges.append(range(int(a), int(b)+1))
    for line in f:
        nums.append(int(line.strip()))

p1 = 0
for num in nums:
    for r in ranges:
        if num in r:
            p1 += 1
            break
print(p1)

p2 = 0
ranges.sort(key=lambda r: r.start)
combined_ranges = [ranges[0]]
for r in ranges[1:]:
    cr = combined_ranges[-1]
    if r.start <= cr.stop:
        combined_ranges[-1] = range(cr.start, max(r.stop, cr.stop))
    else:
        combined_ranges.append(r)

for r in combined_ranges:
    p2 += len(r)
print(p2)
